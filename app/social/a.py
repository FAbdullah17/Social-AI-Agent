import requests
proxies = {
    "http": "socks4://202.166.211.89:60606",
    "https": "socks4://202.166.211.89:60606"
}
try:
    response = requests.get("https://api.twitter.com/2/tweets", proxies=proxies)
    print(response.status_code, response.text)
except Exception as e:
    print("Proxy failed:", str(e))
