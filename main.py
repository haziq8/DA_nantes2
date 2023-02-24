import requests
headers = {
    'User-Agent': 'Mobile'
}
url ='http://172.18.58.80/nantes/'
r = requests.get(url, headers=headers)
print(r.text)
#This will get the status code
print("Status code:")
print("\t*",r.status_code)
#This will just the headers
h = requests.head(url, headers=headers)
print("Header:")
print("****")
#To print line by line
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("****")
