import time
import pprint
import csv
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
import chromedriver_autoinstaller
# from youtube_comment_scraper_python import *
import pandas as pd
import plotly.express as px
import re
import streamlit as st
  
st.title('Youtube WebScrap⛏️')

# # ------------------------------------------------------------------------------CHANNEL DATA------------------------------------------------------------------------
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

chromedriver_autoinstaller.install()
# driver = webdriver.Chrome('/usr/bin/chromedriver') 
chrome_path = '/usr/local/bin/chromedriver'
# # Set up Chrome options if needed
chrome_options = webdriver.ChromeOptions()
# # Create the WebDriver instance
chrome_options.binary_location = chrome_path
driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
# driver = webdriver.Chrome(
#     service=ChromeService(ChromeDriverManager().install()))
# driver.implicitly_wait(5)
# driver = webdriver.Chrome()
url = st.text_input('Paste the Youtube Channel Link',"")
if not url:
  st.warning('Please input a Link.')
  st.stop()
st.success('Thank you for inputting a link.')
# url ='https://www.youtube.com/@YasoobKhalid/videos'
name = re.compile(r"[A-Z]\w+")
inp = name.findall(url)
out = inp[0]
st.write('Getting Data from', out, 'channel')


url = input('Enter Youtube Video Url- ')
driver.get(url)
# # "https://www.youtube.com/@YasoobKhalid/videos"
# channel_title = driver.find_element(By.XPATH, '//yt-formatted-string[contains(@class, "ytd-channel-name")]').text
handle = driver.find_element(By.XPATH, '//yt-formatted-string[@id="channel-handle"]').text
subscriber_count = driver.find_element(By.XPATH, '//yt-formatted-string[@id="subscriber-count"]').text

WAIT_IN_SECONDS = 5
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    # Scroll to the bottom of page
    driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
    # Wait for new videos to show up
    time.sleep(WAIT_IN_SECONDS)
    
    # Calculate new document height and compare it with last height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


thumbnails = driver.find_elements(By.XPATH, '//a[@id="thumbnail"]/yt-image/img')
views = driver.find_elements(By.XPATH,'//div[@id="metadata-line"]/span[1]')
titles = driver.find_elements(By.ID, "video-title")
links = driver.find_elements(By.ID, "video-title-link")
# likes = driver.find_elements(By.ID, "video-title-link-likes")

videos = []
for title, view, thumb, link in zip(titles, views, thumbnails, links):
    video_dict = {
        'title': title.text,
        'views': view.text,
        # 'likes': likes.text,
        'thumbnail': thumb.get_attribute('src'),
        'link': link.get_attribute('href')
    }
    videos.append(video_dict)

print(videos)

to_csv = videos
keys = to_csv[0].keys()

with open(r'C:/Users/ashok/OneDrive/Desktop/WebScrap/Youtube/output/people.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(to_csv)
df = pd.read_csv(r'C:/Users/ashok/OneDrive/Desktop/WebScrap/Youtube/output/people.csv')
st.dataframe(df)
