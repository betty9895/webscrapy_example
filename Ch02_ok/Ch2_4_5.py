import requests 

try:
    r = requests.get("http://www.google.com", timeout=0.03)
    print(r.text)
except requests.exceptions.Timeout as ex:
    print("錯誤: HTTP請求已經超過時間...\n" + str(ex))
    
# 使用timeout參數指定請求時間
# 因請求時間過短，會顯示錯誤訊息
