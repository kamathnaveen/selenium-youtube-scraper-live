import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"
#NDTV_TRENDING_URL ="https://www.ndtv.com/top-stories#pfrom=home-ndtv_topstories"

response = requests.get(YOUTUBE_TRENDING_URL)

print('Status Code', response.status_code)

#print('Output',response.text)

with open('trending.html','w') as f:
  f.write(response.text)

  doc = BeautifulSoup(response.text, 'html.parser')

  print('Page Title',doc.title.text)

  #Find all the video divs
  video_divs = doc.find_all('a',class_='yt-simple-endpoint style-scope ytd-video-renderer')

  print(f'Found {len(video_divs)} videos')