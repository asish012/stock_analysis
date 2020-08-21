import requests
import json
import re
from datetime import date
import copy
from collections import defaultdict

from utils import load_configuration
from src.models.stock import Stock, Stat


BATCH_REQUEST_URL = "https://public-api.quickfs.net/v1/data/batch"

# QFS_FUNDAMENTAL_METRIC = ["revenue", "eps_diluted", "fcf", "total_equity", "price_to_earnings", "ebitda"]
# QFS_FUNDAMENTAL_PERFORMANCE = ["revenue_growth", "eps_diluted_growth", "fcf_growth", "total_equity_growth", "ebitda_growth"]
# QFS_RETURN_METRIC = ["roic", "roa", "roe"]
# QFS_YOY_METRIC = QFS_FUNDAMENTAL_METRIC + QFS_FUNDAMENTAL_PERFORMANCE + QFS_RETURN_METRIC

# QFS_TECHNICAL_METRIC   = ['price_to_earnings', 'market_cap']
# QFS_OTHER_METRIC       = ["eps_diluted",
#                           "price_to_earnings",
#                           "debt_to_equity",
#                           "dividends",
#                           "ebitda",
#                           "enterprise_value",
#                           "market_cap",
#                           "week52high",
#                           "week52low",
#                           "week52change"]


class QuickFS:

    def __init__(self):
        self._name    = "quickfs"
        self._config  = load_configuration(self._name)
        self._api_key = self._config['API_KEY']

    @staticmethod
    def _format_period(period):
        # period="10Y" -> FY-10:FY

        pattern = re.compile(r"\d+[YQ]")
        if pattern.match(period):
            time_frame, time_indicator = (int(period[:-1]) - 1, period[-1:])  # (Number, Year/Quarter)
            return f"period=F{time_indicator}-{time_frame}:F{time_indicator}"
        else:
            raise Exception("Period format mismatch.", period)

    def _get_request_header(self):
        return {'x-qfs-api-key': self._api_key}

    @staticmethod
    def _get_request_body_parts(ticker, stat_key, period):
        return {ticker: f"QFS({ticker}:US,{stat_key},{period})"}

    def _get_request_body(self, ticker, period):
        stat_to_collect = list(Stat().__dict__().keys())
        query_period = self._format_period(period)
        data = defaultdict(dict)

        for s in stat_to_collect:
            data[s] = self._get_request_body_parts(ticker, s, query_period)

        return {"data": data}

    def _collect_metrics_data(self, ticker, period="10Y"):
        print(self._get_request_body(ticker, period))
        # response = requests.post(BATCH_REQUEST_URL,
        #                          json=self._get_request_body(ticker, period),
        #                          headers=self._get_request_header())
        # print(response.status_code, response.reason, response.json())
        # return response.json()
        mock_response = {
            'data': {
                'revenue': {'AMZN': [107006000000, 135987000000, 177866000000, 232887000000, 280522000000]},
                'eps_diluted': {'AMZN': [1.25, 4.9, 6.15, 20.14, 23.01]},
                'fcf': {'AMZN': [7450000000, 10466000000, 8307000000, 19400000000, 25825000000]},
                'total_equity': {'AMZN': [13384000000, 19285000000, 27709000000, 43549000000, 62060000000]},
                'debt_to_equity': {'AMZN': [1.0591, 0.7888, 1.3687, 0.761, 1.0184]},
                'price_to_earnings': {'AMZN': [534.1345, 150.8595, 186.6216, 73.2122, 79.4118]},
                'price_to_sales': {'AMZN': [2.975, 2.6303, 3.1823, 3.1666, 3.2803]},
                'ebitda': {'AMZN': [8514000000, 12302000000, 15584000000, 27762000000, 36330000000]},
                'roic': {'AMZN': [0.0585, 0.1767, 0.1006, 0.2237, 0.1728]},
                'roa': {'AMZN': [0.0099, 0.032, 0.0282, 0.0685, 0.0597]},
                'roe': {'AMZN': [0.0494, 0.1451, 0.129, 0.2827, 0.2194]}
            }
        }
        return mock_response

    @staticmethod
    def _prepare_stock(ticker, stat_data):
        stat = Stat(**stat_data)        # Use the default constructor with **kwargs

        stock = Stock(ticker=ticker)
        stock.stat = stat
        stock._id = ticker
        return stock

    def get(self, ticker, period):
        stat = self._collect_metrics_data(ticker, period)
        return self._prepare_stock(ticker, stat["data"])


# if __name__=="__main__":
#     qfs = QuickFS()
#     print(qfs.collect_data("AMZN", "5Y"))
