import os
import time

import requests

from app.env import env
from app.logger import Logger

_env = env()
logger = Logger('Invitation', filehandler='DEBUG')

class Invitation:
    def __init__(self):...

    def Autoenter(self, invitation:str=None):
        headers = {
            'Referer': f'https://bargain.lol.garena.tw/?token={_env.LCU_Token}',
            'Token': _env.LCU_Token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) LeagueOfLegendsClient/11.15.388.2387 (CEF 74) Safari/537.36',
            'X-CSRFToken': _env.CSRF_Token,
            'Content-Type': 'application/json'
        }
        payload = "{\"code\":\"%s\",\"confirm\":true}" % invitation
        logger.debug(f'輸入邀請碼: {invitation}')
        with requests.post(_env.LOL_Evnet_URL, headers=headers, data=payload) as response:
            if response.status_code != 200:
                pass
            content = response.json()
            logger.debug(content)
            if content.get('error', None) == 'ERROR__TOO_MANY_REQUESTS':
                logger.warning('請求次數過快 休息一下喝杯茶')
                time.sleep(2)
            if (content.get('error', None) == 'ERROR__ENTER_CODE_AMOUNT_OUT_OF_QUOTA'
                or
                content.get('enter_code_amount', None) == 60
                ):
                logger.info('60 個邀請碼已輸入完成')
                os.system("pause")
                exit(0)
            if content.get('enter_code_amount', None):
                count = content.get('enter_code_amount', None)
                logger.info(f'成功輸入第 {count} 個邀請碼')

if __name__ == '__main__':
    invitation = Invitation()
    with open('invitation.txt', 'r', encoding='utf-8') as f:
        invitation_codes = f.readlines()
    for code in invitation_codes:
        invitation.Autoenter(code.replace('\n',''))
    