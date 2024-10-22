from email.header import Header

import requests

url = 'https://www.google.com'
r = requests.get(url)

#### Headers

HEADER = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

### Proxies
WEBSHARE_USERNAME = 'username'
WEBSHARE_PASSWORD = 'password'
PROXY = "http://{}:{}@p.webshare.io:80/".format(WEBSHARE_USERNAME, WEBSHARE_PASSWORD)

proxies = {
    "http": PROXY,
    "https": PROXY
}

r = requests.get(url, proxies=proxies)
r = requests.get(url, proxies=proxies, headers=HEADER)

for i in range(100):
    r = requests.get(url, proxies=proxies)
    if r.status_code == 200:
        print("success")
        break
r = requests.get(url, proxies=proxies, headers=HEADER)

### SCRAPER API
SCRAPER_API_KEY = "someapikey"
r = requests.get('http://api.scraperapi.com?apikey={}&url={}'.format(SCRAPER_API_KEY, url))

### SCRAPING BEE
BEE_API_KEY = "someapikey"
r = requests.get(
    url = 'https://app.scrapingbee.com/api/v1',
    params={
        'apikey': BEE_API_KEY,
        'url': url,
        "block_rescources":'false',
        'premium_proxy':'false',
        'country_code':'us',
        'render_js':'false'
    }
)


from requests_html import HTMLSession
session = HTMLSession()
r = session.get(url)
r.html.render()
print(r.html.render)

