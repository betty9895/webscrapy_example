import requests 

r = requests.get("http://www.google.com/404")
print(r.status_code)
print(r.status_code == requests.codes.ok)

print(r.raise_for_status())

# 取得進一步訊息  raise_for_status()