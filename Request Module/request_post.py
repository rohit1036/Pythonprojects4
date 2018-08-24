import requests,json
url='https://api.github.com/some/endpoint'
'''payload={'some':'data'}
headers={'content-type':'application/json'}
r=requests.post(url,data=json.dumps(payload),headers=headers)
print(r.headers['Content-Type'])
print(r.headers)
print(r.status_code)'''
resp=requests.get(url)
print(resp.status_code)
print(resp.headers)
print(resp.headers['content_type'])