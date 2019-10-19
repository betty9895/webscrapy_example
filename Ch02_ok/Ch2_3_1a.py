import requests

r = requests.get("https://www.google.com")
r.encoding = 'utf-8'
print(r.text)
#text： 解碼後的字元資料，request會依據http標頭來自動解碼。就HTML網頁而言，使用encoding屬性可取得編碼
print("----------------------")

r = requests.get("https://www.google.com")
r.encoding = 'utf-8'
print(r.content)
# content：沒有解碼的位元資料，為二進位的回應內容，適用於非文字內容的請求
print("----------------------")

r = requests.get("https://www.google.com", stream=True)
r.encoding = 'utf-8'
print(r.raw)
print(r.raw.read(15))                                    
# raw：伺服器的原始socket回應(raw socket response)，這是HTTPRespinse物件