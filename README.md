# LoLTW_10Year_88Event

LoLTW 8.8 周年慶 邀請碼自動輸入

# 設定
1. 在 `LoLTW_10Year_88Evnet.exe` 的位置建立一個檔案 `.env`，內容如下
```bash
Bahamut_Discussion = https://forum.gamer.com.tw/C.php?bsn=17532&snA=674866&tnum=15422
Pagelimit = 100
startPage = -1

LCU_Token = 
CSRF_Token = 
LOL_Evnet_URL = https://bargain.lol.garena.tw/api/enter
```
2. 接著要找 LCU_Token 及 CSRF_Token，此處會較為複雜，會利用圖文說明，並**注意 token 請不要讓自己以外的人知道，token 等同於門(帳號)的鑰匙**

 - LCU_Token
    首先先開啟遊戲客戶端並開啟活動頁面，點擊下方的 "個人數據回顧"
    ![](https://imgur.com/d6AxcKd.png)

    此時應該會開啟網頁，並到瀏覽器中找到歷史紀錄(chrome 跟 edge 都是按 ctrl+H)，會發現最上面有 3 個 LOL 的網頁
    ![](https://imgur.com/7b8ruNb.png)

    將第二個點右鍵複製連結，並在空白處貼上就好，**不要貼在聊天室!!!!!**
    ![](https://imgur.com/nyFoBOY.png)

    會發現網址的格式會像是這樣
    ```
    https://datareview.lol.garena.tw/?token=febd56bf3d(打碼)
    ```
    把 token= 後面的字串複製貼到 .env 中的 LCU_Token 即可

 - CSRF_Token
    透過取得 LCU_Token 之後就可以拿到 CSRF_Token
    請先將這個網址複製到瀏覽器中
    ```
    https://bargain.lol.garena.tw/?token=
    ```
    token 後面所接的就是上個步驟取得的 LCU_Token  
    所以這邊會變成類似
    ```
    https://bargain.lol.garena.tw/?token=febd56bf3d(打碼)
    ```
    在瀏覽器打開這個網址會發現就是活動的頁面，接著點網址列上的綠色鎖頭，然後點選 Cookie (Chrome 跟 edge 都大同小異)
    ![](https://imgur.com/zUEXTsS.png)

    接著展開 `bargain.lol.garena.tw` > `Cookie` > `csrftoken`，之後下面的內容點滑鼠左鍵兩下就會全部反白，然後複製起來貼到 .env 中的 CSRF_Token 就可以了
    ![](https://imgur.com/bHIBcIA.png)

爬蟲的頁面邀請碼抓取的條件為 `Pagelimit` 和 `startPage`  
`Pagelimit` 指的是最多會抓取幾頁的邀請碼，如預設值 100 就是抓取 100 個頁面的邀請碼  

`startPage` 指的是最後頁面，因為最開始設計是從最新的貼文開始抓邀請碼，所以抓取頁面是倒序抓取，如預設值為 -1 時則由程式自行判斷該討論串的最後一頁

範例1: Pagelimit=100 startPage=-1，而在當時該討論串最後一頁為 800，那爬蟲就會爬取 800~700 頁的邀請碼

範例2: Pagelimit=50 startPage=200，那爬蟲就會爬取 200~150 頁的邀請碼