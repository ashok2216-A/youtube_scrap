import time
import pprint
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
# from youtube_comment_scraper_python import *
import pandas as pd
import plotly.express as px
import re
import streamlit as st

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")

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
