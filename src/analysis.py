
from src.clients.quickfs import *


def main():
    ticker = "MSFT"
    # stock = Stock(ticker)
    # stock.fetch_data()

    client = QuickFS()
    stock = client.get(ticker)
    print(stock)

if __name__=="__main__":
    main()
