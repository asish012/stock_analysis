from iexfinance.stocks import Stock
from utils import load_configuration

MILLION = 1000000000


class FundamentalsAnalysis:
    def __init__(self, ticker):
        self.ticker = ticker
        config = load_configuration('iexfinance.cfg')
        self.stock = Stock(self.ticker, token=config['token'])
        # print(stock.get_earnings(period='annual', last=4))

    def get_revenue(self):
        income_satements = self.stock.get_income_statement(period='annual', last=4)
        total_revenues = [{statement['reportDate']: statement['totalRevenue']/MILLION} for statement in income_satements if 'totalRevenue' in statement]
        return total_revenues

    def get_eps(self):
        '''TODO: Get EPS from other source because here it only returns previous 4 quarters'''
        earnings = self.stock.get_earnings(period='annual', last=4)
        eps = [{e['EPSReportDate']: e['actualEPS']} for e in earnings if 'actualEPS' in e]
        return eps

    def get_equity(self):
        balance_sheet = self.stock.get_balance_sheet(period='annual', last=4)
        equities = [{balance['reportDate']: balance['shareholderEquity'] / MILLION} for balance in balance_sheet['balancesheet'] if 'shareholderEquity' in balance]
        return equities

    def get_free_cash_flow(self):
        cash_flow = self.stock.get_cash_flow(period='annual', last=4)
        free_cash_flows = [{cash['reportDate']: (cash['cashFlow'] + cash['capitalExpenditures']) / MILLION}
                           for cash in cash_flow['cashflow'] if 'cashFlow' in cash and 'capitalExpenditures' in cash]
        return free_cash_flows

    def __str__(self):
        report = dict()
        report['revenue'] = self.get_revenue()
        report['eps'] = self.get_eps()
        report['equity'] = self.get_equity()
        report['free_cash_flow'] = self.get_free_cash_flow()
        return str(report)


analysis = FundamentalsAnalysis('GOOGL')
print(analysis)
