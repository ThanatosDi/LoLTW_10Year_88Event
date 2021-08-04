import os

from app.env import env
from app.invitation import Invitation
from app.logger import Logger
from app.spider import Spider

spider = Spider()
_env = env()
invitation = Invitation()
logger = Logger('main', filehandler='DEBUG')
__version__ = '1.0.2'
__author__ = 'ThanatosDi'


if __name__ == '__main__':
    logger.info(f'LoLTW_10Year_88Event Version:{__version__} Author:{__author__}')

    if 'forum.gamer.com.tw' in _env.Bahamut_Discussion:
        logger.info('發現網址為: 巴哈姆特')
        Pagelimit = spider.fetch().page_limit()

        if _env.startPage != -1:
            Pagelimit = _env.startPage

        logger.info(f'爬取頁面範圍: {Pagelimit-_env.Pagelimit}~{Pagelimit}')

    with open('invitation.txt', 'w', encoding='utf-8') as f:
        if 'forum.gamer.com.tw' in _env.Bahamut_Discussion:
            logger.info('爬取巴哈姆特邀請碼中...')
            for page in range(Pagelimit, Pagelimit-_env.Pagelimit, -1):
                invitation_codes = spider.fetch(page=page).filter()
                f.write('\n'.join(invitation_codes))
                f.write('\n')
        else:
            invitation_codes = spider.fetch().filter()
            f.write('\n'.join(invitation_codes))
            f.write('\n')

    logger.info('開始自動輸入邀請碼')
    with open('invitation.txt', 'r', encoding='utf-8') as f:
        invitation_codes = f.readlines()
    for code in invitation_codes:
        invitation.Autoenter(code.replace('\n',''))
    logger.info('邀請碼已輸入結束')
    os.system('pause')
