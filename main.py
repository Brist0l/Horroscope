import requests
from bs4 import BeautifulSoup

response= requests.get("https://www.horoscope.com/zodiac-signs")

if response.status_code == 200:
    print("Website is up!")
else:
    # todo: Add check_internet()
    print("Website is Down!")
    exit(1)
soup=BeautifulSoup(response.content,'html.parser')
print(soup.title)
