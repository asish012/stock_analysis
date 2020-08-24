import attr
import json


@attr.s(repr=False)
class Stat:
    revenue = attr.ib(default=[])
    eps_diluted = attr.ib(default=[])
    fcf = attr.ib(default=[])
    total_equity = attr.ib(default=[])
    debt_to_equity = attr.ib(default=[])
    price_to_earnings = attr.ib(default=[])
    price_to_sales = attr.ib(default=[])
    ebitda = attr.ib(default=[])
    roic = attr.ib(default=[])
    roa = attr.ib(default=[])
    roe = attr.ib(default=[])

    @classmethod
    def from_dict(cls, stat_data):
        print("""
        ----- This is a manual approach to prepare Stat object from quickfs statistics
        ----- Instead, use the default constructor (with **kwargs) passing quickfs statistics as dict
        """)
        stat = Stat()
        if "revenue" in stat_data:
            stat.revenue = stat_data["revenue"]
        if "eps_diluted" in stat_data:
            stat.eps_diluted = stat_data["eps_diluted"]
        if "fcf" in stat_data:
            stat.fcf = stat_data["fcf"]
        if "total_equity" in stat_data:
            stat.total_equity = stat_data["total_equity"]
        if "debt_to_equity" in stat_data:
            stat.debt_to_equity = stat_data["debt_to_equity"]
        if "price_to_earnings" in stat_data:
            stat.price_to_earnings = stat_data["price_to_earnings"]
        if "price_to_sales" in stat_data:
            stat.price_to_sales = stat_data["price_to_sales"]
        if "ebitda" in stat_data:
            stat.ebitda = stat_data["ebitda"]
        if "roic" in stat_data:
            stat.roic = stat_data["roic"]
        if "roa" in stat_data:
            stat.roa = stat_data["roa"]
        if "roe" in stat_data:
            stat.roe = stat_data["roe"]
        return stat

    def __repr__(self):
        return json.dumps(attr.asdict(self))

    def __dict__(self):
        return attr.asdict(self)


@attr.s(repr=False)
class Stock:
    ticker = attr.ib(kw_only=True)
    # company_name = attr.ib(default=str())
    stat = attr.ib(default=Stat())

    # current_debt = attr.ib(default=float())
    # current_equity = attr.ib(default=float())
    # current_debt_to_equity = current_debt/current_equity
    # current_eps = attr.ib(default=float())
    # current_pe = attr.ib(default=float())
    # current_price_to_sales = attr.ib(default=float())
    # 52wkhigh = attr.ib(default=float())
    # 52wklow = attr.ib(default=float())
    # forward_pe = attr.ib(default=float())
    # forward_peg = attr.ib(default=float())

    def __repr__(self):
        return json.dumps(attr.asdict(self))

    def __dict__(self):
        return attr.asdict(self)
