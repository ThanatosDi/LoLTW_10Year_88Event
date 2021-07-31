import os
from app.spider import Spider
from app.invitation import Invitation
from app.env import env
spider = Spider()
_env = env()
invitation = Invitation()

if __name__ == '__main__':

    Pagelimit = spider.fetch().page_limit()

    if _env.startPage != -1:
        Pagelimit = _env.startPage

    print(f'爬取頁面範圍: {Pagelimit-_env.Pagelimit}~{Pagelimit}')

    with open('invitation.txt', 'a', encoding='utf-8') as f:
        for page in range(Pagelimit, Pagelimit-_env.Pagelimit, -1):
            invitation_codes = spider.fetch(page=page).filter()
            f.write('\n'.join(invitation_codes))
            f.write('\n')

    with open('invitation.txt', 'r', encoding='utf-8') as f:
        invitation_codes = f.readlines()
    for code in invitation_codes:
        invitation.Autoenter(code.replace('\n',''))