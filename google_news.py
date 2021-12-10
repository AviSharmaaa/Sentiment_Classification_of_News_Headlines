from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

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

root = "https://www.google.com/"
link = "https://www.google.com/search?q=cds+bipin+rawat&rlz=1C1CHBF_enIN912IN912&tbm=nws&sxsrf=AOaemvLePTsPOGUWiTuUmVM19M3rbk8aJQ:1639163511323&source=lnt&tbs=qdr:d&sa=X&ved=2ahUKEwj5wsf299n0AhUMzzgGHZHCAP4QpwV6BAgBECE&biw=540&bih=746&dpr=1.25"


def get_news(link):
    req = Request(link, headers=hdrs)
    webpage = urlopen(req).read()
    with requests.Session():
        soup = BeautifulSoup(webpage, "html5lib")
        for i in range(10):
            get_headlines(soup)
            go_to_next_page(soup)


def go_to_next_page(soup):
    next_page = soup.find('a', attrs={'class': 'nBDE1b G5eFlf'})
    next_page = (next_page['href'])
    link = root + next_page


def get_headlines(soup):
    for item in soup.find_all('h3', attrs={'class': 'zBAuLc l97dzf'}):
        title = (item.find('div', attrs={'class':
                                         'BNeawe vvjwJb AP7Wnd'})).get_text()
        title = title.replace(",", "")
        document = open('data.csv', 'a')
        document.write('{}, \n'.format(title))
        document.close()


get_news(link)
