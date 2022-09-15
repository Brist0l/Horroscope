import requests
from bs4 import BeautifulSoup

import check_internet
from args import Parser

star_sign = Parser().get_star_sign()
print(star_sign)

response = requests.get(f"https://www.horoscope.com/zodiac-signs/{star_sign}")

if not response.status_code == 200:
    print("Some Connection Error\nChecking Internet!")
    if check_internet.is_connected(check_internet.REMOTE_SERVER):
        print("Internet Is Available\nWebsite Is Down")
        exit(1)

soup = BeautifulSoup(response.content, 'html.parser')

# for para in soup.find_all("p"):
#     print(para.get_text())
