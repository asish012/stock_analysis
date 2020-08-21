from src.clients.quickfs import QuickFS
from utils.db import get_mongo_client

db = get_mongo_client()
table = db.stocks

if __name__=="__main__":
    qfs = QuickFS()

    ticker = "AMZN"
    stock = qfs.get(ticker, "5Y")
    stock = stock.__dict__()
    stock["_id"] = ticker

    print(stock)

    stored_stock = table.find_one(stock)
    if not stored_stock:
        table.insert_one(stock)
