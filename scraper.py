import csv

from bs4 import BeautifulSoup
import requests

#
# with open('countries.txt', 'r') as f:
#     urls = f.readlines()
#
# for count,ele in enumerate(urls):
#     urls[count] = urls[count].rstrip("\n")

urls = ['https://en.wikipedia.org/wiki/Afghanistan']

class Country:
    def __init__(self, name, size, pop, capital):
        self.name = name
        self.size = size
        self.pop = pop
        self.capital = capital

# scrape elements
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    country = soup.find("span", class_="mw-page-title-main").get_text

    capP1 = soup.find_all("th", class_="infobox-label")
    capital = ""
    for item in capP1:
        print(item)
        # if (capP1.get_text == "Capital"):
        #     capital = item.findNext("a").get_text
    print(capital)
    print(country)
