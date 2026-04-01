#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("Error: requests library not found. Install with: pip install requests", file=sys.stderr)
    sys.exit(1)

try:
    from mutagen import File as MutagenFile
except ImportError:
    print("Error: mutagen library not found. Install with: pip install mutagen", file=sys.stderr)
    sys.exit(1)


NOW_FILE = Path("content/now.md")
EPISODES_FILE = Path("data/pocketcasts_episodes.json")
POCKETCASTS_API = "https://api.pocketcasts.com"
AUDIO_FETCH_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "audio/mpeg,audio/*;q=0.9,*/*;q=0.8",
    "Referer": "https://pocketcasts.com/",
}


def parse_json_response(response: requests.Response, action: str) -> dict:
    """Return parsed JSON or raise a helpful error when the API contract changes."""
    content_type = response.headers.get("Content-Type", "")
    if "json" not in content_type.lower():
        body_preview = response.text.strip().replace("\n", " ")[:200]
        raise RuntimeError(
            f"Pocket Casts returned unexpected content for {action}: "
            f"HTTP {response.status_code}, Content-Type '{content_type or 'unknown'}', body '{body_preview}'"
        )

    try:
        return response.json()
    except json.JSONDecodeError as error:
        raise RuntimeError(f"Pocket Casts returned invalid JSON for {action}: {error}") from error


def get_credentials() -> tuple[str, str]:
    """Get Pocket Casts credentials from 1Password vault."""
    try:
        # Get email from 1Password
        email = subprocess.check_output(
            ["op", "read", "op://Personal/pocketcasts/username"],
            text=True
        ).strip()
        
        # Get password from 1Password
        password = subprocess.check_output(
            ["op", "read", "op://Personal/pocketcasts/password"],
            text=True
        ).strip()
        
        if not email or not password:
            raise RuntimeError("Empty credentials retrieved from 1Password")
        
        return email, password
    
    except FileNotFoundError:
        raise RuntimeError("1Password CLI (op) not found. Install from https://1password.com/downloads/command-line/")
    except subprocess.CalledProcessError as error:
        raise RuntimeError(
            f"Failed to retrieve Pocket Casts credentials from 1Password. "
            f"Ensure the item exists at op://Personal/pocketcasts with 'username' and 'password' fields. "
            f"Error: {error}"
        )


def authenticate(email: str, password: str) -> str:
    """Authenticate with Pocket Casts API and return token."""
    url = f"{POCKETCASTS_API}/user/login"
    payload = {
        "email": email,
        "password": password,
        "scope": "webplayer"
    }

    response = requests.post(url, json=payload, timeout=30)
    data = parse_json_response(response, "authentication")

    if not response.ok:
        message = data.get("errorMessage") or data.get("message") or response.reason
        raise RuntimeError(f"Pocket Casts authentication failed: {message}")

    token = data.get("token") or data.get("access_token") or data.get("jwt")
    if not token:
        raise RuntimeError(
            "Pocket Casts authentication succeeded but no token was returned. "
            f"Response keys: {', '.join(sorted(data.keys())) or 'none'}"
        )

    return token


def get_podcast_titles(token: str) -> dict[str, str]:
    """Fetch subscribed podcasts and map UUIDs to titles."""
    url = f"{POCKETCASTS_API}/user/podcast/list"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(url, headers=headers, json={"v": 1}, timeout=30)
    data = parse_json_response(response, "podcast list lookup")
    if not response.ok:
        message = data.get("errorMessage") or data.get("message") or response.reason
        raise RuntimeError(f"Pocket Casts podcast list lookup failed: {message}")

    return {
        podcast.get("uuid", ""): podcast.get("title", "Unknown Podcast")
        for podcast in data.get("podcasts", [])
        if podcast.get("uuid")
    }


def format_duration(total_seconds: int) -> str:
    """Format duration seconds as H:MM:SS or M:SS."""
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    if hours > 0:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    return f"{minutes}:{seconds:02d}"


def get_duration_from_audio_url(url: str) -> str:
    """Download an audio file and return its formatted duration using mutagen."""
    parsed = urlparse(url)
    suffix = Path(parsed.path).suffix or ".mp3"

    with requests.get(url, headers=AUDIO_FETCH_HEADERS, stream=True, timeout=60) as response:
        response.raise_for_status()
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=True) as temp_file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    temp_file.write(chunk)
            temp_file.flush()

            audio = MutagenFile(temp_file.name)
            if not audio or not getattr(audio, "info", None) or not getattr(audio.info, "length", None):
                return ""

            try:
                return format_duration(int(audio.info.length))
            except (TypeError, ValueError):
                return ""


def get_recent_episodes(token: str, days: int = 7) -> list[dict]:
    """Fetch recently played episodes from the past N days."""
    url = f"{POCKETCASTS_API}/history/list"
    headers = {"Authorization": f"Bearer {token}"}
    podcast_titles = get_podcast_titles(token)

    response = requests.post(url, headers=headers, json={}, timeout=30)
    data = parse_json_response(response, "history lookup")
    if not response.ok:
        message = data.get("errorMessage") or data.get("message") or response.reason
        raise RuntimeError(f"Pocket Casts history lookup failed: {message}")

    episodes = []
    duration_cache: dict[str, str] = {}
    
    # Calculate the cutoff date
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)
    
    for change in data.get("changes", []):
        if change.get("action") != 1:
            continue

        modified_at_raw = change.get("modifiedAt")
        if not modified_at_raw:
            continue

        try:
            played_at = datetime.fromtimestamp(int(modified_at_raw) / 1000, tz=timezone.utc)
        except (TypeError, ValueError):
            continue

        if played_at >= cutoff_date:
            podcast_uuid = change.get("podcast", "")
            episode_url = change.get("url", "https://www.pocketcasts.com/")
            duration_formatted = duration_cache.get(episode_url, "")
            if not duration_formatted and episode_url.startswith("http"):
                try:
                    duration_formatted = get_duration_from_audio_url(episode_url)
                except requests.RequestException:
                    duration_formatted = ""
                duration_cache[episode_url] = duration_formatted
            
            episodes.append({
                "show": podcast_titles.get(podcast_uuid, "Unknown Podcast"),
                "episode": change.get("title", "Unknown Episode"),
                "url": episode_url,
                "duration": duration_formatted
            })
    
    return sorted(episodes, key=lambda x: x["show"])


def format_episodes_json(episodes: list[dict]) -> str:
    """Format episodes as JSON string."""
    return json.dumps(episodes, indent=2)


def update_last_updated(now_lines: list[str], updated_on: str) -> list[str]:
    """Update the Last Updated timestamp."""
    for index, line in enumerate(now_lines):
        if line.startswith("Last Updated: "):
            now_lines[index] = f"Last Updated: {updated_on}"
            break
    
    return now_lines


def main() -> int:
    try:
        # Get credentials
        email, password = get_credentials()
        
        # Authenticate
        print("Authenticating with Pocket Casts...")
        token = authenticate(email, password)
        
        # Fetch recent episodes
        print("Fetching recent episodes...")
        episodes = get_recent_episodes(token, days=7)
        
        if not episodes:
            print("No episodes found in the past 7 days.", file=sys.stderr)
            return 1
        
        print(f"Found {len(episodes)} episodes")
        
        # Write episodes to JSON file
        episodes_json = format_episodes_json(episodes)
        EPISODES_FILE.write_text(episodes_json + "\n")
        print(f"Updated {EPISODES_FILE} with {len(episodes)} episodes")
        
        # Update Last Updated timestamp in now.md
        now_lines = NOW_FILE.read_text().splitlines()
        updated_on = datetime.now().strftime("%d-%b-%Y")
        updated_lines = update_last_updated(now_lines, updated_on)
        NOW_FILE.write_text("\n".join(updated_lines) + "\n")
        print(f"Updated Last Updated timestamp in {NOW_FILE}")
        
        return 0
    
    except RuntimeError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    except requests.RequestException as error:
        print(f"API Error: {error}", file=sys.stderr)
        return 1
    except Exception as error:
        print(f"Unexpected error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
