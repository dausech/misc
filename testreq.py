import requests
ret = requests.get('http://www.dausech.me/', timeout=1)
print(ret.content)

