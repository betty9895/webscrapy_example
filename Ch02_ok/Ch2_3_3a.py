import requests 

r = requests.get("http://www.google.com")

print(r.headers.get('Content-Type'))
print(r.headers.get('Content-Length'))
print(r.headers.get('Date'))
print(r.headers.get('Server'))
print(r.headers.get('Cookie'))

# 呈現結果同Ch2_3_3.py，這種寫法比較好