import requests 

data = {'name': 'ouyuru', 'score': 95}
r = requests.get("http://httpbin.org/get", params=data)
print(r.text)

""" 
r = requests.get("http://httpbin.org/cookies/set", params=data)
print(r.text)
"""


# A simple HTTP Request & Response Service web：   http://httpbin.org/