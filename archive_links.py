import os
import re
import requests
from datetime import datetime, timedelta
import yaml

# Path to your Hugo site content folder
content_path = os.path.join(os.getcwd(), "content")

# Regular expression to find markdown links: [link_text](link_url)
md_link_pattern = re.compile(r'\[.*?\]\((https?://.*?)\)')

# Regular expression to parse frontmatter in Hugo markdown files
frontmatter_pattern = re.compile(r'^---(.*?)---', re.DOTALL)

# Wayback Machine URL prefix
wayback_machine_prefix = "https://web.archive.org/"

def parse_frontmatter(md_file):
    """
    Parse the frontmatter of a markdown file to extract the post date.
    """
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    frontmatter_match = re.match(frontmatter_pattern, content)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        try:
            # Load frontmatter as YAML and extract the 'date' field
            frontmatter_data = yaml.safe_load(frontmatter)
            post_date = frontmatter_data.get('date')
            if post_date:
                return datetime.strptime(post_date, '%Y-%m-%d')
        except yaml.YAMLError:
            pass
    
    return None

def query_wayback_machine(url):
    """
    Query the Wayback Machine API to check if a URL has been archived.
    """
    api_url = f"http://archive.org/wayback/available?url={url}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if data['archived_snapshots']:
                closest_snapshot = data['archived_snapshots']['closest']
                if closest_snapshot['available']:
                    return closest_snapshot['timestamp']
    except requests.RequestException as e:
        print(f"Error querying Wayback Machine for {url}: {e}")
    
    return None

def find_external_links(md_file):
    """
    Parse a markdown file to find external links that don't point to the Wayback Machine.
    """
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all URLs in markdown file
    external_links = re.findall(md_link_pattern, content)

    # Filter out Wayback Machine URLs
    external_links = [url for url in external_links if not url.startswith(wayback_machine_prefix)]

    return external_links

def check_markdown_files(root_folder):
    """
    Traverse the Hugo content directory and check markdown files for external links.
    """
    for subdir, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".md"):
                md_file_path = os.path.join(subdir, file)
                external_links = find_external_links(md_file_path)
                post_date = parse_frontmatter(md_file_path)

                if external_links and post_date:
                    for url in external_links:
                        archive_timestamp = query_wayback_machine(url)
                        
                        if archive_timestamp:
                            # Convert the archive timestamp to datetime
                            archive_date = datetime.strptime(archive_timestamp, '%Y%m%d%H%M%S')
                            # Check if the archive date is within one day of the post date
                            if abs((archive_date - post_date).days) <= 1:
                                continue

                        # If no valid archive found, or it’s not within 1 day of the post date
                        print(f"File: {md_file_path}")
                        print(f"  External Link: {url}")

# Run the script
check_markdown_files(content_path)
