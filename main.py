from bs4 import BeautifulSoup
import requests
import csv


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
                price = float(html_listings[2].get_text().strip().replace(",", "").replace("$", ""))
                change = html_listings[3].get_text().strip()
                volume =float(html_listings[4].get_text().strip().replace(",", "").replace("$", ""))
                value = float(html_listings[5].get_text().strip().replace(",", "").replace("$", ""))
                capitalisation = float(html_listings[6].get_text().strip().replace(",", "").replace("$", ""))
                market_listings.append([code, company, price, change, volume, value, capitalisation])


        with open(market+ "_data.csv", "a", encoding="UTF-8") as toWrite :
            writer = csv.writer(toWrite)
            print(market_listings)
            writer.writerows(market_listings)


get_market("NZSX")
