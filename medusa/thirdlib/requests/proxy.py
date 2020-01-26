import requests
proxies = {
    "http": "http://127.0.0.1:1080",
    "https": "https://127.0.0.1:1080",
}

r = requests.get("http://cip.cc", proxies=proxies)
# requests.get("http://cip.cc")
print(r.text)