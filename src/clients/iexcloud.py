from iexfinance.stocks import Stock
from utils import load_configuration
import pandas as pd

MILLION = 1000000000


class Fundamentals:
    # custom_search_url = 'https://cloud.iexapis.com/stable/stock/ADBE/quote/latestPrice?token=IEXTOKEN'
    def __init__(self, ticker):
        config = load_configuration('iexfinance')
        self._stock = Stock(ticker, token=config['API_KEY'])
        print(self._stock.get_price())
        # self.company_name = str()
        # self.fundamentals = pd.DataFrame()
        # self.advanced_stats = {}
        # # self.debt_to_equity = None
        # # self.forward_pe = None
        # # self.peg = None

        # self._collect_stats()
        # self._get_advanced_stats()

    # def _get_revenue(self):
    #     income_statements = self._stock.get_income_statement(period='annual', last=4)
    #     total_revenues = {statement['reportDate']: statement['totalRevenue']/MILLION for statement in income_statements if 'totalRevenue' in statement}
    #     return pd.Series(total_revenues)
    #
    # def _get_eps(self):
    #     '''TODO: Get EPS from other source because here it only returns previous 4 quarters'''
    #     earnings = self._stock.get_earnings(period='annual', last=4)
    #     eps = {e['EPSReportDate']: e['actualEPS'] for e in earnings if 'actualEPS' in e}
    #     return pd.Series(eps)
    #
    # def _get_equity(self):
    #     balance_sheet = self._stock.get_balance_sheet(period='annual', last=4)
    #     equities = {balance['reportDate']: balance['shareholderEquity'] / MILLION for balance in balance_sheet['balancesheet'] if 'shareholderEquity' in balance}
    #     return pd.Series(equities)
    #
    # ''' Free cash flow = Operating cash flow - Capital expenditure
    #     In IEXCloud capitalExpenditures is provided as negative value already '''
    # def _get_free_cash_flow(self):
    #     cash_flow = self._stock.get_cash_flow(period='annual', last=4)
    #     free_cash_flow = {cash['reportDate']: (cash['cashFlow'] + cash['capitalExpenditures']) / MILLION
    #                       for cash in cash_flow['cashflow'] if 'cashFlow' in cash and 'capitalExpenditures' in cash}
    #     return pd.Series(free_cash_flow)
    #
    # def _get_roic(self):
    #     income_statements = self._stock.get_income_statement(period='annual', last=4)
    #     # roic = {(cash['netIncome'] / cash['investments']) for cash in cash_flow['cashflow']}
    #     # return roic
    #     return income_statements
    #
    # def _get_advanced_stats(self):
    #     key_stats = self._stock.get_key_stats(period='annual', last=4)
    #
    #     # # debt_to_equity < 0.5 is very good; < 1 is okay; > 1 is bad; > 2 is very bad;
    #     # if 'debtToEquity' in key_stats:
    #     #     self.advanced_stats['debt_to_equity'] = key_stats['debtToEquity']
    #     # if 'forwardPERatio' in key_stats:
    #     #     self.advanced_stats['forward_pe'] = key_stats['forwardPERatio']
    #     if 'companyName' in key_stats:
    #         self.company_name = key_stats['companyName']
    #     if 'ttmEPS' in key_stats:
    #         self.advanced_stats['eps_ttm'] = key_stats['ttmEPS']
    #     if 'peRatio' in key_stats:
    #         self.advanced_stats['pe_ratio'] = key_stats['peRatio']
    #     if 'sharesOutstanding' in key_stats:
    #         self.advanced_stats['shares_outstanding'] = key_stats['sharesOutstanding']
    #     if 'marketcap' in key_stats:
    #         self.advanced_stats['marketcap'] = key_stats['marketcap']
    #     if 'week52high' in key_stats:
    #         self.advanced_stats['week52high'] = key_stats['week52high']
    #     if 'week52low' in key_stats:
    #         self.advanced_stats['week52low'] = key_stats['week52low']
    #     if 'week52change' in key_stats:
    #         self.advanced_stats['week52change'] = key_stats['week52change']
    #
    # def _collect_stats(self):
    #     self.fundamentals['total_revenue'] = self._get_revenue()
    #     # self.fundamentals['eps'] = self._get_eps()
    #     self.fundamentals['shareholders_equity'] = self._get_equity()
    #     self.fundamentals['free_cash_flow'] = self._get_free_cash_flow()


if __name__ == '__main__':
    analysis = Fundamentals('GOOGL')
    print(analysis.__dict__)
