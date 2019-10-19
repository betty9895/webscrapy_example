import requests 

url = "https://api.github.com/user"

# 送出需認證的http請求 (auth=github 帳號,密碼)
r = requests.get(url, auth=('betty9895@gmail.com', 'Nominwoo0731'))
if r.status_code == requests.codes.ok:
    print(r.headers['Content-Type'])
    print(r.json())
else:
    print("HTTP請求錯誤...")