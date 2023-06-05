from bs4 import BeautifulSoup #for scraping
import requests               #required for reading the file
import pandas as pd           #(optional) Pandas for dataframes 
import json                   #(optional) If you want to export json
import os


url = input('Enter Youtube Video Url- ') # user input for the link
Vid={}
Link = url
source= requests.get(url).text
soup=BeautifulSoup(source,'lxml')
div_s = soup.findAll('div')
Title = div_s[1].find('span',class_='watch-title').text.strip()
Vid['Title']=Title
Vid['Link']=Link
Channel_name = div_s[1].find('a',class_="yt-uix-sessionlink spf-link").text.strip()
Channel_link = ('www.youtube.com'+div_s[1].find('a',class_="yt-uix-sessionlink spf-link").get('href'))
Subscribers = div_s[1].find('span',class_="yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count").text.strip()
if len(Channel_name) ==0:
    Channel_name ='None'
    Channel_link = 'None'
    Subscribers = 'None'
Vid['Channel']=Channel_name
Vid['Channel_link']=Channel_link
Vid['Channel_subscribers']=Subscribers