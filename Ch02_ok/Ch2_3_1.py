import requests

r = requests.get("http://google.com")

print(r.text)
print(r.encoding)

r = requests.get("http://google.com")
r.encoding = 'utf-8'

print(r.text)
print(r.encoding)