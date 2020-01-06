import requests

host = 'tail1'

r = requests.get('https://www.baidu.com')
r.encoding = 'utf-8'
print(r.text)