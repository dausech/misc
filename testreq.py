import requests
ret = requests.get('http://www.dausech.me/acc101', timeout=1)
print(ret.content)

