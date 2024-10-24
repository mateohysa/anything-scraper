import os
from dotenv import load_dotenv
load_dotenv()
PROXY = os.getenv('PROXY')
proxies = {
                "http": PROXY,
                "https": PROXY
    }
RALLY_USERNAME = os.getenv('RALLY_USERNAME')
RALLY_PASSWORD = os.getenv('RALLY_PASSWORD')
import requests
import pandas as pd
import string
from bs4 import BeautifulSoup
import re
import cloudscraper
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--disable-gpu')
userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
chrome_options.add_argument(f'user-agent={userAgent}')

def get_rally_data():
    for i in range(0,10):
        try:
            url = "https://api-kube.production.rallyrd.com/api/v2/assets/"
            headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
            payload = {"email":RALLY_USERNAME, "password":RALLY_PASSWORD, "remember_me":True}
            scraper = cloudscraper.create_scraper()
            raw = scraper.post(url, headers=headers, json=payload)
            rawson = raw.json()
            jwttoken = rawson['jwttoken']
            headers = {"Authorization": f"Bearer {jwttoken},Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
            r = scraper.get(url, headers=headers)
            rson = r.json
            break
        except:
            pass
    return rson["items"]

if __name__ == "__main__":
    r = get_rally_data()
    print(r)


