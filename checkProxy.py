import requests

from get_cookie import getNewCookie

MAX_RETRY = 1
MAX_TIMEOUT=1


for i in range(0,256):
    proxy = f'TV4GO0:1Z7dhD8iey@188.130.137.{str(i)}:5500'
    proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}', }
    for i in range(0, MAX_RETRY):
        try:
            # cookieTTT='x_wbaas_token=1.1000.7b88182a45834cda9c19d83a11475855.MHwxNzYuMTUuMTY0LjI1fE1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xNDQuMC4wLjAgU2FmYXJpLzUzNy4zNnwxNzcxNTkxODg1fHJldXNhYmxlfDJ8ZXlKb1lYTm9Jam9pSW4wPXwwfDN8MTc3MDk4NzA4NXwx.MEUCIAfklxTyrKkvNX6hoUuTR76ETN+XljS1AVVOCxNrmQ0oAiEAit/4Nq2BDq58hjH4uGPjb1SQN5fWp/j4fErNB2n7eEY=; _wbauid=9255161901770382035; routeb=1770404947.732.60.384847|28979c6168ec4738f0fcb8539a6d5f12'
            response = requests.get(
                timeout=MAX_TIMEOUT,
                url='https://api.ipify.org/',
                proxies=proxies
            )
            if response.status_code == 200:
                #getNewCookie(proxy, None)
                print(proxy)
        except : pass
