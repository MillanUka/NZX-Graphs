from bs4 import BeautifulSoup
import requests
import csv
import re

def get_market(market):
        markets_url = "https://www.nzx.com/markets/" + market

        response = requests.get(markets_url)
        soup = BeautifulSoup(response.text, "html.parser")

        count = 0

        market_listings = []
        market_listings.append(["Code", "Company", "Price", "Change", "Volume", "Value", "Capitalisation"])
        for rows in soup.find_all("tr"):
            count += 1
            if(count > 1):
                html_listings = rows.find_all("td")
                code = html_listings[0].get_text().strip()
                company = html_listings[1].get_text().strip()
                try:
                     price = float(re.sub('[^0-9.]','', html_listings[2].get_text().strip()))
                except:
                    price = 0
                change = html_listings[3].get_text().strip()
                try:
                    volume = float(re.sub('[^0-9.]','', html_listings[4].get_text().strip()))
                except:
                    volume = 0
                
                try:
                    value = float(re.sub('[^0-9.]','', html_listings[5].get_text().strip()))
                except:
                    value = 0

                try:
                    capitalisation = float(re.sub('[^0-9.]','', html_listings[6].get_text().strip()))
                except:
                    capitalisation = 0

                market_listings.append([code, company, price, change, volume, value, capitalisation])


        # with open(market+ "_data.csv", "a", encoding="UTF-8") as toWrite :
        #     writer = csv.writer(toWrite)
        #     writer.writerows(market_listings)

        return market_listings


markets = []

markets.append(get_market("NZSX"))
markets.append(get_market("NZDX"))
markets.append(get_market("NZZX"))

del(markets[0][0])
del(markets[1][0])
del(markets[2][0])

exec(open("drawGraphs.py").read())


