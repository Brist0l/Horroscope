import requests
from bs4 import BeautifulSoup

import check_internet
from src import args

star_sign = args.Parser().get_star_sign()

response = requests.get(f"https://www.horoscope.com/zodiac-signs/{star_sign}")

if response.status_code == 200:
    pass
else:
    print("Some Connection Error\nChecking Internet!")
    if check_internet.is_connected(check_internet.REMOTE_SERVER):
        print("Internet Is Available\nWebsite Is Down")
        exit(1)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.title)

image_list = []

images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    image_list.append({"src": src, "alt": alt})

for image in image_list:
    print(image)
