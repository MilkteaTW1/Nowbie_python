import requests
from bs4 import BeautifulSoup
#解析Html擴充

header = {
    'Referer':'https://ssr1.scrape.center/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
# 偽造請求

url = "https://ssr1.scrape.center/"
#爬蟲靶場

response = requests.get(url=url,headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
result = soup.find_all(name='div')