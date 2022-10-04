from src.config import EtlConfig
from currency_converter import CurrencyConverter


class CurrencyCaller:
    c = CurrencyConverter()
    
    @staticmethod
    def get_currency_dict(currency_range):
        return {k: CurrencyCaller.c.convert(1, k, EtlConfig.currency_base) for k in currency_range}