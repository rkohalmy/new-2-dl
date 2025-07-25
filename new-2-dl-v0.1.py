# First step is to identify videos from a chanel and get the video IDs for ytdl. S
# Scrape Chanel for video ID and time/date of video publish. 

from bs4 import BeautifulSoup
import requests

url="https://youtube.com/feeds/videos.xml?user=Destiny"
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")

for entry in soup.find_all("entry"):
    for videoid in entry.find_all("yt:videoID"):
        print(videoid)
    for published in entry.find_all("published")

# compare published date/time to current date/time 