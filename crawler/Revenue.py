class Revenue:
    pass

from iexfinance.stocks import Stock
import json

aapl = Stock("AAPL", token='pk_8dacda7ce2f940efbc2837e15147551b')
data = aapl.get_earnings(period='annual', last=4)
print(data)
