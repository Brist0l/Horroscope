import requests
from bs4 import BeautifulSoup

import args
import check_internet

star_sign = args.Parser().get_star_sign()

response = requests.get("https://www.horoscope.com/zodiac-signs")

if response.status_code == 200:
    print("Website is up!")
else:
    print("Some Connection Error\nChecking Internet!")
    if check_internet.is_connected(check_internet.REMOTE_SERVER):
        print("Internet Is Available\nWebsite Is Down")
        exit(1)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.title.name)
