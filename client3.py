# Made By Iolo Evans Jones For The Forage JP Morgan Software Engineering Work Experience
import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2  # Updated this line
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b == 0:  # Added this line
        return
    return price_a / price_b  # Updated this line


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        prices = {}  # Added this line
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price  # Added this line
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        # Assumed that we have 'ABC' and 'DEF' as stocks in the quotes
        print("Ratio %s" % getRatio(prices['ABC'], prices['DEF']))  # Updated this line
