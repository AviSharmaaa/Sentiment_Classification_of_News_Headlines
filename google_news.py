import os.path
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

ROOT = "https://www.google.com/"

hdrs = {
    'User-Agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}


def delete_file():
    flag = os.path.exists('data.csv')

    if flag:
        open_file = open("data.csv",'a')
        open_file.seek(0)
        open_file.truncate()

def get_news(link):
    req = Request(link, headers=hdrs)
    webpage = urlopen(req).read()
    document = open('data.csv', 'a')
    document.write('{} \n'.format('Heading'))
     
    with requests.Session():
        soup = BeautifulSoup(webpage, "html5lib")
        for _ in range(100):
            get_headlines(soup,document)
            go_to_next_page(soup)
    document.close()


def go_to_next_page(soup):
    next_page = soup.find('a', attrs={'class': 'nBDE1b G5eFlf'})
    next_page = (next_page['href'])
    link = ROOT + next_page


def get_headlines(soup,document):
    for item in soup.find_all('h3', attrs={'class': 'zBAuLc l97dzf'}):
        title = (item.find('div', attrs={'class':
                                         'BNeawe vvjwJb AP7Wnd'})).get_text()
        title = title.lower()
        title = title.replace(',','')
        title = title.replace(':',"")
        title = title.replace('%','')
        title = title.replace(' ...','')
        title = title.replace("'","")
        document.write('{} \n'.format(title))
