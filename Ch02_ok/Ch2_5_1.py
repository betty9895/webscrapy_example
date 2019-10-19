import requests 

url = 'http://www.google.com/404'

try:
    r = requests.get(url, timeout=3)
    r.raise_for_status()
except requests.exceptions.RequestException as ex1:
    print("Http請求錯誤: " + str(ex1))
except requests.exceptions.HTTPError as ex2:
    print("Http回應錯誤: " + str(ex2))
except requests.exceptions.ConnectionError as ex3:
    print("網路連線錯誤: " + str(ex3))
except requests.exceptions.Timeout as ex4:
    print("Timeout錯誤: " + str(ex4))    


""" 
requests例外物件 
RequestException    HTTP請求有誤的時候會產生此例外物件
HTTPError           回應不合法獨HTTP回影內容時會產生此例外物件
ConnectionError     當網路連線或ＤＮＳ錯誤時就會產生此例外物件
Timeout             當HTTP請求超過指定期限時就會產生此例外物件
TooManyRedirects    如果重新轉址超過設定的最大值時就會逞生此例外物件
 """
