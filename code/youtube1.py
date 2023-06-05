import time
import pprint
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
from youtube_comment_scraper_python import *
import pandas as pd
import plotly.express as px
import re
import streamlit as st

st.title('Youtube Channel Analysis')
st.write('Youtube WebScrap')


# # ------------------------------------------------------------------------------CHANNEL DATA------------------------------------------------------------------------

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


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
driver.get(url)

# url = input('Enter Youtube Video Url- ')
# driver.get(url)
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

with open('output/people.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(to_csv)
df = pd.read_csv('output/people.csv')
st.dataframe(df)

count = st.slider('Select Lower Video Count', 0, 607, 100)
st.write("You selected", count, 'Videos')

fig = px.bar(df,
    x="title",
    y="views", height=600
)
fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
# fig.update_yaxes(tickvals=['10k', '22k', '29k', '56k'])
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)

# ----------------------------------------------------------------------------COMMENTS------------------------------------------------------------------------------


# url = input('Enter Youtube Video Url- ')
# youtube.open(url)
# youtube.keypress("pagedown")

# data = []
# currentpagesource=youtube.get_page_source()
# lastpagesource=''

# while(True):
#     if(lastpagesource==currentpagesource):
#         break
        
#     lastpagesource=currentpagesource
#     response=youtube.video_comments()

#     for c in response['body']:
#         data.append(c)
        
#     youtube.scroll()
#     currentpagesource=youtube.get_page_source()


# df = pd.DataFrame(data)

# df = df.replace('\n',' ', regex=True)

# df = df[['Comment', 'Likes']].drop_duplicates(keep="first") 
# # df = df[['Likes']].drop_duplicates(keep="first") 

# df.to_csv('output/data.csv',index=False) 

# df.head()