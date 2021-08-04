import re

import requests
from bs4 import BeautifulSoup

from app.env import env
from app.logger import Logger

_env = env()
logger = Logger('Spider', filehandler='DEBUG')

class Spider():
    
    def __init__(self):...

    def fetch(cls, page:int=None):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
        }
        params = {
            'page': page
        }
        logger.debug(f'爬取頁面: {page}')
        with requests.get(_env.Bahamut_Discussion, headers=headers, params=params) as response:
            if response.status_code != 200:
                logger.error('爬蟲請求發生錯誤 %s' % response.status_code)
            cls.body = response.text
            return cls

    def filter(self):
        bs4 = BeautifulSoup(self.body, 'html.parser')
        matches = re.finditer(r'LOL[A-Z,0-9]{10}', bs4.text, re.MULTILINE)
        for match in matches:
            yield match.group()

    def page_limit(self) -> int:
        bs4 = BeautifulSoup(self.body, 'html.parser')
        pagebtnA = bs4.find('p', {'class': 'BH-pagebtnA'}).find_all('a')
        logger.debug(f'爬取最後一頁頁數: {int(pagebtnA[-1].text)}')
        return (int(pagebtnA[-1].text))

if __name__ == '__main__':
    spider = Spider()

    Pagelimit = spider.fetch().page_limit()

    print(f'爬取頁面範圍: {Pagelimit-_env.Pagelimit}~{Pagelimit}')

    with open('invitation.txt', 'a', encoding='utf-8') as f:
        for page in range(Pagelimit, Pagelimit-_env.Pagelimit, -1):
            invitation = spider.fetch(page=page).filter()
            f.write('\n'.join(invitation))
            f.write('\n')

    