from src.config import CurrencyConfig
from datetime import datetime
from currency_converter import CurrencyConverter


class CurrencyCaller:
    def __init__(self):
        self.currency_base = CurrencyConfig.currency_base
        self.currency_list = CurrencyConfig.currency_list
        self.c = CurrencyConverter()

    def get_currency(self, currency):
        return self.c.convert(1, self.currency_base, currency)

    def get_all_currencies(self, date):
        return [{"dt": date,  "code": i, "rate": self.get_currency(i)} for i in self.currency_list]

