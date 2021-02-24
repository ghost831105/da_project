# test 1
#%%  import
import urllib.request as req
import json
import shutil
import requests
import bs4


url = "https://building-management.publicwork.ntpc.gov.tw/bm_query.jsp?rt=3"

#%% 抓取驗證碼
img_url = "https://building-management.publicwork.ntpc.gov.tw/ImageServlet"
res = requests.get(img_url, stream=True, verify=False)
with open("img/check.png", "wb") as f:
    shutil.copyfileobj(res.raw, f) 

from IPython.display import Image
Image("img/check.png") # 無法正確顯示

#%% 獲取資料

url = "https://building-management.publicwork.ntpc.gov.tw/bm_list.jsp" # 含表格資料的網址
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    "Content-Type":"text/html",
    } 
payloadData = {
    "rt":"BM",
    "PagePT": "0",
    "A2V":"%A8%CF%A5%CE%B0%F5%B7%D3", # 職照類型:  使用執照
    "D1V":"%B7s%A5_%A5%AB%AAO%BE%F4%B0%CF", # 建築地址-行政區
    "D3":"%A4T%A5%C1", # 建築地址-路街段
    "D1":"220", #新北市板橋區
    "Z1":"4305" # 看check.png 的驗證碼號碼輸入
    }
payloadData = json.dumps(payloadData).encode("utf-8")

request = req.Request(url, data=payloadData, headers=headers)
with req.urlopen(request) as r:
    r = r.read().decode('Big5') # 獲取網路原始碼, 文本的編譯方式: Big5 
    print(r) # 是否取得需要的資料?  失敗
root = bs4.BeautifulSoup(r, 'html.parser') # 解析 html



