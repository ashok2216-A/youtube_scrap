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
import numpy as np

st.title('Youtube Channel Analysis📈')

df = pd.read_csv(r'C:/Users/ashok/OneDrive/Desktop/WebScrap/Youtube/output/people.csv')
st.dataframe(df)

count = st.slider('Select Lower Video Count', 0, len(df), 100)
st.write("You selected", count, 'Videos')


fig = px.bar(df[:count],
    x="title",
    y="views", height=1000
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
