from iexfinance.stocks import Stock
from utils import load_configuration


class FundamentalDataCollecgtor:
    def __init__(self, ticker):
        self.ticker = ticker

config = load_configuration('iexfinance.cfg')
aapl = Stock("AAPL", token=config['token'])
data = aapl.get_earnings(period='annual', last=4)
print(data)
