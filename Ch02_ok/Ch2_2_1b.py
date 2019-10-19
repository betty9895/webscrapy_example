import requests 

""" 
url_params = {'name': 'ouyuru', 'score': 95}
r = requests.get("http://httpbin.org/get", params=url_params)
r = requests.get("https://www.google.com/search",params=url_params)
print(r.url) 
 """

def googleSearch(query):
    with requests.session() as c:
        url = 'https://www.google.co.in'
        query = {'q': query}
        r = requests.get(url, params=query)
        print (r.url)

googleSearch('apple')
