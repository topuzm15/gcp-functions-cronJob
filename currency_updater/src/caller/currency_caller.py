from src.config import CurrencyConfig
from datetime import datetime as date
from currency_converter import CurrencyConverter


class CurrencyCaller:
    def __init__(self):
        self.currency_base = CurrencyConfig.currency_base
        self.currency_list = CurrencyConfig.currency_list
        self.c = CurrencyConverter()

    def get_currency(self, currency):
        return self.c.convert(1, self.currency_base, currency)

    def get_all_currencies(self):
        return [{"dt": date.today().strftime("%Y-%m-%d"),  "code": i, "rate": self.get_currency(i)} for i in self.currency_list]

