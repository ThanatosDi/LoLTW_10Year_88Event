import os

from dotenv import load_dotenv


class env():
    def __init__(self):
        load_dotenv(override=True)

    @property
    def Bahamut_Discussion(self) -> str:
        return os.getenv('Bahamut_Discussion', '')
        
    @property
    def Pagelimit(self) -> int:
        Pagelimit = os.getenv('Pagelimit', 100)
        try:
            Pagelimit = int(Pagelimit)
        except Exception:
            return 100
        else:
            return Pagelimit

    @property
    def startPage(self) -> int:
        startPage = os.getenv('startPage', -1)
        try:
            startPage = int(startPage)
        except Exception:
            return -1
        else:
            return startPage

    @property
    def LCU_Token(self) -> str:
        return os.getenv('LCU_Token', '')

    @property
    def CSRF_Token(self) -> str:
        return os.getenv('CSRF_Token', '')

    @property
    def LOL_Evnet_URL(self) -> str:
        return os.getenv('LOL_Evnet_URL', '')