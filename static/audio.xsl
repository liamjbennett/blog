<?xml version="1.0" encoding="utf-8"?>

<!-- 
	XSL HTML TRANSFORM FOR AUDIO
-->

<xsl:stylesheet
	version="1.0"
	xml:lang="en-SG"
	xmlns="http://www.w3.org/1999/xhtml"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:str="http://exslt.org/strings"
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:dcterms="http://purl.org/dc/terms/"
	xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
    extension-element-prefixes="str">

	<!-- Metadata about this file; xsl will ignore top-level elements it doesn't recognise -->
	<rdf:RDF>
		<rdf:Description rdf:about="https://rubenerd.com/opml.xsl">
			<dcterms:creator>Liam Bennett</dcterms:creator>
			<dcterms:title>liamjbennett Audio XSLT</dcterms:title>
			<dcterms:description>A template to transform RSS (Audio) XML into HTML</dcterms:description>
			<dcterms:format>application/xslt+xml</dcterms:format>
			<dcterms:created>2024-04-01T14:37:00+11:00</dcterms:created>
			<dcterms:modified>2024-04-01T14:37:00+11:00</dcterms:modified>
			<dcterms:license rdf:resource="https://opensource.org/licenses/BSD-3-Clause"/>
		</rdf:Description>
	</rdf:RDF>

	<xsl:output method="html" indent="yes" media-type="text/html" encoding="utf-8" doctype-public="HTML" doctype-system=""/>

	<!-- Kludge to create permalinks from text titles (work-in-progress) -->
	<xsl:variable name="lowercase">abcdefghijklmnopqrstuvwxyz--</xsl:variable>
	<xsl:variable name="uppercase">ABCDEFGHIJKLMNOPQRSTUVWXYZ .</xsl:variable>

	<xsl:template match="/">
		<html lang="en-SG">
			<head>
				<title></title>
				<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
				<style type="text/css">
					@charset "utf-8";
					body {
						background:white url("/haruhiism@2x.png") fixed bottom right no-repeat;
						background-size:140px 149px;
						border-top:10px solid #585757;
						color:black;
						font:1em "Helvetica Neue","Liberation Sans",Arial,sans-serif;
						line-height:24px;
						margin:0;
						overflow-y:scroll;
						padding:40px 40px 200px 40px
					}
					h1      { letter-spacing:-1px }
					a       { color:#009199 }
					a:hover { text-decoration:none }
					li      { list-style-type:none }
                    
					#nav a { margin-right:0.6em }

                    /* Formatting using table */
                    table {
                        margin: 20px;
                        table-layout:fixed;
                        width: 800px;
						border: 0px solid;
                    }

                    th, td {
                        border: 0px solid;
						padding: 5px;
                    }

					.postItem {
						border: 1px solid;
					}

                    .image-cell {
                        padding-right: 10px;
                        width: 140px;
                    }

					.title {
						font-size: 20px;
						font-weight: bold;
					}

                    /* Adding an image */
                    td img {
                        width: 140px; /* Adjust image size as needed */
                        height: auto;
                        vertical-align: middle; /* Aligns the image vertically within its container */
                    }

					
				</style>
			</head>
			<body>
				<h1>An RSS feed of all podcasts with audio recordings</h1>
				<p id="nav">
					<a href="/posts">Blog</a>
					<a href="/feed.xml">RSS</a>
				</p>
				<xsl:for-each select="/rss/channel/item">
					<div class="postItem">
						<table>
							<tr>
								<xsl:variable name="podImage" select="//*[local-name()='image']/@href"/>
								<td class="image-cell" rowspan="4"><img src="{$podImage}" alt="missing podcast image"/></td>
								<td class="title">
									<xsl:value-of select="title"/>
								</td>
							</tr>
							<tr>
								<td><xsl:value-of select="description"/></td>
							</tr>
							<tr>
								<td>
									<audio controls="">
										<xsl:variable name="guid" select="guid"/>
										<source src="{$guid}" type="audio/mpeg"/>
									</audio>
								</td>
							</tr>
							<tr>
								<td>
									<xsl:variable name="inputDate" select="pubDate" />
									<xsl:variable name="formattedDate">
										<xsl:value-of select="substring($inputDate, 6, 2)" /> <!-- Month -->
										<xsl:text> </xsl:text>
										<xsl:value-of select="substring($inputDate, 9, 3)" /> <!-- Day -->
										<xsl:text>, </xsl:text>
										<xsl:value-of select="substring($inputDate, 13, 4)" /> <!-- Year -->
									</xsl:variable>
									
									<xsl:variable name="inputTime">
										<xsl:value-of select="itunes:duration"/>
										<xsl:text> </xsl:text>
									</xsl:variable>
									<xsl:variable name="minutes" select="number(substring($inputTime,4,2))" />
									<xsl:variable name="seconds" select="number(substring($inputTime,7,2))" />
									
				
									<xsl:value-of select="$formattedDate" /> - <xsl:value-of select="concat($minutes, ' min ', $seconds, ' seconds')" />
								</td>
							</tr>
						</table>
					</div>
				</xsl:for-each>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>
