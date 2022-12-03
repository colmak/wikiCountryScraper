from bs4 import BeautifulSoup
import requests
from pathlib import Path

with open('countries.txt', 'r') as f:
    urls = f.readlines()

for count,ele in enumerate(urls):
    urls[count] = urls[count].rstrip("\n")

# urls = ['https://en.wikipedia.org/wiki/Afghanistan']



# scrape elements
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    country = soup.find("span", class_="mw-page-title-main").get_text(strip=True)

    table = soup.find('table', class_="vcard")

    labels = table.findAll("th", class_="infobox-label")
    headers = table.findAll("th", class_="infobox-header")

    for label in labels:
        # print(label.get_text(strip=True))
        if (label.get_text(strip=True).__contains__("Capital")):
            capital = label.findNext("a").get_text()
        if (label.get_text(strip=True).__contains__("2022 estimate")):
            pop = label.findNext("td", class_="infobox-data").get_text().split("[")[0]
        if (label.get_text(strip=True).__contains__("Density")):
            density = label.findNext("td", class_="infobox-data").get_text().split("(")[0].strip()
        if (label.get_text(strip=True).__contains__("HDI")):
            HDI = label.findNext("td", class_="infobox-data").get_text().split("[")[0].strip()
        if (label.get_text(strip=True).__contains__("Calling code")):
            calling_code = label.findNext("td", class_="infobox-data").get_text().split("[")[0].strip()
        if(label.get_text(strip=True).__contains__("Legislature")):
            legislature = label.findNext("a").get_text()
        if(label.get_text(strip=True).__contains__("Demonym")):
            Demonym = label.findNext("a").get_text()
        if (label.get_text(strip=True).__contains__("Official")):
            language = label.findNext("td", class_="infobox-data").findNext("a").get_text()
        if (label.get_text(strip=True).__contains__("Currency")):
            currency = label.findNext("a").get_text()


    for header in headers:
        if (header.get_text(strip=True).__contains__("Area")):
            area = header.findNext("td", class_="infobox-data").get_text().split("[")[0]

    dataOut = open("dataExport.csv", "a")
    dataOut.write(country+"#"+capital+"#"+language+"#"+currency+"#"+legislature+"#"+pop+"#"+HDI+"#"+calling_code+"#"+density+"#"+area +"\n")


    # print(language)
    # print(currency)
    # print(legislature)
    # print(pop)
    # print(HDI)
    # print(calling_code)
    # print(density)
    # print(area)
    # print(capital)
    # print(country)
    #
