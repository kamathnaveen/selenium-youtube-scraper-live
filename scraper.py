import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"
#NDTV_TRENDING_URL ="https://www.ndtv.com/top-stories#pfrom=home-ndtv_topstories"


def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--headless')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_videos(driver):
  VIDEO_DIV_TAG = 'ytd-video-renderer' # Tag used to pull videos
  driver.get(YOUTUBE_TRENDING_URL)
  videos = driver.find_elements(By.TAG_NAME,VIDEO_DIV_TAG)
  return videos

def parse_video(video):
  title_tag = video.find_element(By.ID,'video-title')
  url = title_tag.get_attribute('href')

  thumbnail_tag = video.find_element(By.TAG_NAME,'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')

  channel_div = video.find_element(By.CLASS_NAME,'ytd-channel-name')
  channel_name = channel_div.text

  views_div = video.find_element(By.CLASS_NAME,'ytd-video-meta-block')
  views = views_div.text

  description = video.find_element(By.ID, 'description-text').text

  return {
    'Title': title_tag.text,
    'url':url,
    'thumbnail_url' : thumbnail_url,
    'Channel' : channel_name,
    'Description': description
  }

if __name__ == "__main__"  :
  print("Creating driver")
  driver = get_driver()
 
  print("Fetching Trending Videos")
  videos = get_videos(driver)
  
 
  print(f'Found {len(videos)} videos')

  print("Parsing the top 10 video")
  # title , video url , thumbnail url , channel, views, uploaded,description

  #video = videos[0] 
  videos_data = [parse_video(video) for video in videos[:10]]

  #print(videos_data)
  

  print("Saving the data to csv")

  videos_df = pd.DataFrame(videos_data)
  print(videos_df)
  videos_df.to_csv('Trending.csv')