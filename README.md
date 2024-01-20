# Wiki Country Scraper

One example showcasing the data we collected

![image](https://github.com/colmak/wikiCountryScraper/assets/69098858/c90bf4ea-77de-40c9-b9e0-7839de2aa262)


## Description
This project involves web scraping information about countries from Wikipedia using Python's BeautifulSoup library. The script extracts data such as country name, capital, language, currency, legislature, population, HDI (Human Development Index), calling code, population density, and area. The collected data is then exported to a CSV file named "dataExport.csv."

## Prerequisites
Make sure you have the following installed before running the script:
- Python 3
- BeautifulSoup library
- Requests library

You can install the required libraries using the following commands:
```bash
pip install beautifulsoup4
pip install requests
```

## Usage
1. Create a text file named 'countries.txt' with the list of Wikipedia URLs for the countries you want to scrape. Each URL should be on a separate line.

2. Run the script using the following command:
```bash
python script.py
```

3. The script will iterate through the provided URLs, extract the required information, and append it to the "dataExport.csv" file.

## Example 'countries.txt'
```
https://en.wikipedia.org/wiki/Afghanistan
https://en.wikipedia.org/wiki/United_States
# Add more URLs as needed
```

## Output Format (dataExport.csv)
The exported CSV file will have the following format:
```
Country#Capital#Language#Currency#Legislature#Population#HDI#Calling Code#Density#Area
Afghanistan#Kabul#Pashto and Dari#Afghan afghani#Islamic Republic#39,000,000#0.511#93#+93#56/sq mi#652,230 sq km
United States#Washington, D.C.#English#United States dollar#Federal government#331,000,000#0.926#+1#93/sq mi#9,631,418 sq km
# Data for additional countries will be appended
```

Note: Some values may contain additional information in square brackets, and the script attempts to remove such information.

## Disclaimer
This script is for educational and informational purposes only. Ensure compliance with the terms of service of the websites you are scraping. The developer is not responsible for any misuse of this script.
