#Scraping YouTube Data
#Scraping the YouTube Video Likes using Selenium and Python & Creating Web Application (Streamlit)

**Introduction to Web Scraping:**

Web scraping is the automated process of extracting information or data from websites. It involves writing a script or using software to access and gather data from web pages, transforming unstructured data on the web into a structured format that can be analyzed, stored, or used in various applications.

**Web Scraping Process:**

Access Websites: A script or program accesses web pages, mimicking human browsing behavior.
Retrieve Data: It extracts specific information from these web pages.
Organize Data: The extracted data is structured and saved in a usable format (like CSV, JSON, or a database).
Fetching Data: The process starts with a request to a website, retrieving the HTML content.
Parsing: The HTML content is parsed to identify and extract relevant information using techniques like Regular Expressions, XPath, or CSS selectors.
Data Extraction: The desired data, such as text, images, links, or tables, is extracted from the parsed HTML.
Storage/Analysis: Extracted data is stored locally or analyzed for insights, automation, or integration into other systems.

What is Selenium?

Selenium scraping refers to using the Selenium framework, primarily employed for automating web browsers, to extract data from websites. It's a powerful tool used in web scraping to simulate human interaction with a web page by controlling a browser programmatically.
Tools Required
To get started, ensure you have the following tools installed:
Python: A programming language used for scripting.
Selenium WebDriver: A tool for controlling web browsers programmatically.
Streamlit: It will help to deploy a App.

Here's how it works:
Automating Web Browsers: Selenium allows you to control a web browser (like Chrome, Firefox, or others) programmatically. It mimics human interaction by opening web pages, clicking buttons, filling forms, and navigating across different pages.

2. Data Extraction: Once the browser is directed to a particular webpage, Selenium enables the extraction of desired data. This can include scraping text, images, tables, or any other content from the webpage.
3. Scraping Dynamic Content: Selenium is particularly useful for scraping websites with dynamic content that can't be easily accessed using traditional scraping libraries.
4. Complex Scraping Scenarios: Selenium is versatile and can handle complex scraping tasks that involve interactions such as login processes, submitting forms, scrolling through infinite scroll pages, or dealing with content behind logins or captchas.
Import Libraries:
import time
import pprint
import csv
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
from youtube_comment_scraper_python import *
import pandas as pd
import plotly.express as px
import re
import streamlit as st
Kickstart with Selenium WebDriver:
The Selenium WebDriver is a key component of the Selenium framework, designed to facilitate the interaction between your code and web browsers. It allows you to automate the testing of web applications and perform web scraping tasks by controlling browsers programmatically.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = st.text_input('Paste the Youtube Channel Link',"")
if not url:
  st.warning('Please input a Link.')
  st.stop()
st.success('Thank you for inputting a link.')
name = re.compile(r"[A-Z]\w+")
inp = name.findall(url)
out = inp[0]
st.write('Getting Data from', out, 'channel')

driver.get(url)
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
Extracting Channel Information:
YouTube channels hold a wealth of information, from engaging content to vital statistics that provide insights into their popularity. In this guide, we'll explore how to programmatically extract key details like the channel's title, views, thumbnail, and link using Python's web scraping tools.
Extracting the Title, Views, Thumbnail, Link of the YouTube channel
Channel Title: Locate the HTML element containing the channel's title.
Channel Views: Find and extract the total number of views the channel has amassed.
Thumbnail URL: Extract the URL of the channel's thumbnail image.
Channel Link: Obtain the link to the YouTube channel.

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
Storing Scraped Data in CSV format
videos is a list of dictionaries containing the data to be written to the variable to_csv.
csv.DictWriter is a class within Python's csv module that facilitates writing data from dictionaries into CSV files. It's particularly useful when you have data organized in a dictionary format and want to export it into a CSV file with well-defined headers.
The code uses the csv module to write data to a CSV file named data.csv.
Then, it utilizes the pandas library (pd) to read the CSV file into a pandas DataFrame (df) and write that DataFrame to an CSV file. abd read the file named people.csv using the pd.read_csv() method.

to_csv = videos
keys = to_csv[0].keys()

with open(r'C:/Users/ashok/OneDrive/Desktop/WebScrap/Youtube/output/data.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(to_csv)
df = pd.read_csv(r'C:/Users/ashok/OneDrive/Desktop/WebScrap/Youtube/output/peop.csv')
st.dataframe(df)
Streamlit App Development and Deployment:
Streamlit is a Python library for creating web applications with minimal effort :D
Streamlit is a Python library for creating web applications with minimal effort:
Streamlit • A faster way to build and share data apps
Rapid Development: Enables building interactive web apps using simple Python scripts.
2. Data Visualization: Seamlessly integrates with popular data science libraries like Pandas, Matplotlib, and Plotly for quick data visualization.
3. Automatic Updates: Auto-refreshes the app when code changes are detected, providing a smooth development experience.
4. Custom Components: Supports custom HTML, CSS, and JavaScript for advanced customization.
5. Deployment: Supports deployment to various platforms, including Streamlit sharing, Heroku, or other cloud providers.

Scrapping YouTube Data using Selenium and Python - YouTube
Conclusion
Automating the extraction of YouTube channel details using Python and web scraping techniques can save time and provide valuable insights. By harnessing the power of libraries like Selenium you can effortlessly retrieve crucial statistics like the channel's title, views, thumbnail, and link for further analysis or integration into your projects.
Start exploring and extracting valuable data from YouTube channels effortlessly with Python!
