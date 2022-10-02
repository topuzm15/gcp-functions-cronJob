from datetime import datetime, timedelta
from loguru import logger
from src.caller import CurrencyCaller
from src.model import CurrencyDataModel
from src.validation import CurrencyRequestValidation


class CurrencyUpdater:
    data_model = CurrencyDataModel()
    currency_caller = CurrencyCaller()

    def get_currency_data(date=datetime.today().strftime("%Y-%m-%d")):
        logger.info("Calling currency api for date: {date}", date=date)
        return CurrencyUpdater.currency_caller.get_all_currencies(date)

    def insert_currency_data_in_range(start_date, end_date):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        while start_date <= end_date:
            temp_end_date = start_date + timedelta(days=1)
            data = CurrencyUpdater.get_currency_data(date=start_date.strftime("%Y-%m-%d"))
            logger.info("delete operation between {start_date} and {end_date}", start_date=start_date.strftime("%Y-%m-%d"), end_date=temp_end_date.strftime("%Y-%m-%d"))
            delete_result = CurrencyUpdater.data_model.delete_data(start_date.strftime("%Y-%m-%d"), temp_end_date.strftime("%Y-%m-%d"))
            insert_result = CurrencyUpdater.data_model.insert_currency_data(data)
            start_date = temp_end_date

    @staticmethod
    def insert_currency_data():
        data = CurrencyUpdater.get_currency_data()
        delete_result = CurrencyUpdater.data_model.delete_data((datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d"),
                                                                datetime.today().strftime("%Y-%m-%d"))
        insert_result = CurrencyUpdater.data_model.insert_currency_data(data)

        return f'Operation completed successfully'


    @staticmethod
    def apply_operation(payload: CurrencyRequestValidation):
        if payload.operation_type == "insert":
            CurrencyUpdater.insert_currency_data_in_range(payload.start_date, payload.end_date)
            return "Insert Operation completed successfully"
        elif payload.operation_type == "delete":
            CurrencyUpdater.data_model.delete_data(payload.start_date, payload.end_date)
            return "Delete Operation completed successfully"
        else:
            return f"Invalid operation type: {payload.operation_type}"