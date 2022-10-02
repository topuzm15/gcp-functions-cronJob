from loguru import logger
from src import CurrencyUpdater, CurrencyRequestValidation

import os

def http_currency_updater(request):
    request_json = request.get_json()
    logger.info("Request body: {request}", request=request_json)

    logger.info(os.listdir(os.curdir))
    try:
        CurrencyUpdater.insert_currency_data()
    except Exception as e:
        logger.error("Error while updating currency data: {error}", error=e)
        return f"Error in currency updater"
    return f'Operation completed successfully'