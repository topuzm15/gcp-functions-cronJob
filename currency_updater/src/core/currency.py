from datetime import datetime, timedelta
from src.caller import CurrencyCaller
from src.model import CurrencyDataModel


class CurrencyUpdater:
    data_model = CurrencyDataModel()

    def get_currency_data():
        currency_caller = CurrencyCaller()
        return currency_caller.get_all_currencies()

    @staticmethod
    def insert_currency_data():
        data = CurrencyUpdater.get_currency_data()
        delete_result = CurrencyUpdater.data_model.delete_data((datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d"),
                                                      datetime.today().today().strftime("%Y-%m-%d"))
        insert_result = CurrencyUpdater.data_model.insert_currency_data(data)

    @staticmethod
    def insert_currency_data_in_range(start_date, end_date):
        data = CurrencyUpdater.get_currency_data()
        delete_result = CurrencyUpdater.data_model.delete_data(start_date, end_date)
        insert_result = CurrencyUpdater.data_model.insert_currency_data(data)
