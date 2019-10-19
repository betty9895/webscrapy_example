import requests 

r = requests.get("http://www.google.com")
print(r.status_code)
print(r.status_code == requests.codes.ok)

r = requests.get("http://www.google.com/404")
print(r.status_code)
print(r.status_code == requests.codes.ok)

r = requests.get("http://www.google.com")
print(r.status_code)
print(r.status_code == requests.codes.all_good)


# 檢查請求式成功可使用
# requests.codes.ok | requests.code.all_good (兩個回應狀態碼一樣)

# status_code==200              =>請求成功
# 400  <= status_code  <=  599  =>請求有誤
# status_code==404              =>網頁不存在 