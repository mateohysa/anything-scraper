import os
from dotenv import load_dotenv
load_dotenv()
PROXY = os.getenv("PROXY")
proxies = {
    "http": PROXY,
    "https": PROXY
}
import requests
import pandas as pd
import string

def scrape_bestsellers(site_url):
    url = site_url+"json"
    r = requests.get(url, proxies=proxies)
    data = r.json()
    return data["products"]

if __name__ == "__main__":
    site_url = "https://www.shopify.com/" #this can be the url of the shopify site
    data = scrape_bestsellers(site_url)
    df = pd.DataFrame(data)
    df.to_csv("bestsellers.csv")

