###this crawler can be used to extract contact info such as email from the instagram search results of a certain group of people (in this case writers)
import os

import requests
import regex as re
from dotenv import load_dotenv
load_dotenv()
PROXY = os.getenv('PROXY')
proxies = {
                "http": PROXY,
                "https": PROXY
    }
import requests as rq
import pandas as pd
import string
from bs4 import BeautifulSoup

def get_soup(url):
    headers = {"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    r = requests.get(url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def prepare_keywords():
    # keywords = []
    keywords1 = list(string.ascii_lowercase)
    # product of combinations of 2 letters
    # keywords2 = [a+b for a in keywords1 for b in keywords1]
    # # product of combinations of 3 letters
    # # keywords3 = [a+b+c for a in keywords1 for b in keywords1 for c in keywords1]
    # keywords = keywords2  + keywords1
    return keywords1


def scrape_duckduckgo(keyword):
    url="https://www.duckduckgo.com/?q="+keyword
    results = []
    try:
        soup = get_soup(url)
        links = soup.find_all("a", class_="result__snippet")

        for l in links:
            details = {}
            details["url"] = l["href"]
            details["snippet"] = l.text
            # extract email using regex from string
            emails = re.findall(r'[\w\.-]+@[\w\.-]+', details["snippet"])
            details["email"] = emails[0].rstrip(".") if len(emails) > 0 else ""
            results.append(details)
    except:
        pass
    return results

def scrape_more_duckduckgo(keyword):
    helper_keywords = prepare_keywords()
    keywordlist = [keyword+" "+k for k in helper_keywords]
    # print(keywordlist)
    results = []
    for k in keywordlist[:4]:
        print(keywordlist.index(k),"/",len(keywordlist))
        try:
            results += scrape_duckduckgo(k)
        except:
            pass
    return results

if __name__ == "__main__":

    #you can use the exact same thing for @outlook or @protonmail emails, same goes for the niche, you can do fitness or whatever
    query = "site:instagram.com @gmail.com writer"
    data = scrape_more_duckduckgo(query)
    df = pd.DataFrame(data)
    df = df.drop_duplicates(subset=["url"])
    df.to_csv("leads.csv",index=False)



