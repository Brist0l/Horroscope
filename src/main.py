#!/bin/python3

import requests
from bs4 import BeautifulSoup

import check_internet
from args import Parser
from datetime import date

star_sign = Parser().get_star_sign()

def get_info(soup):
    for para in soup.find_all("p"):
         print(para.get_text())


# Internet Check
if requests.get('https://www.astrology.com/').status_code != 200:
    print("Some Connection Error\nChecking Internet!")
    if check_internet.is_connected(check_internet.REMOTE_SERVER):
        print("Internet Is Available\nWebsite Is Down")
        exit(1)


if Parser().get_args() == "today":
    print(f"\nDaily Horroscope For {date.today()} is:\n")
    response = requests.get(f"https://www.astrology.com/horoscope/daily/{star_sign}.html") # daily horrorscope 
    soup = BeautifulSoup(response.content, 'html.parser')
    get_info(soup)
else:
    response = requests.get(f"https://www.astrology.com/zodiac-signs/{star_sign}") # description
    soup = BeautifulSoup(response.content, 'html.parser')
    get_info(soup)
