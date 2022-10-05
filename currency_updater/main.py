from loguru import logger
from src import CurrencyUpdater, CurrencyRequestValidation

def http_currency_updater(request):
    request_json = request.get_json()
    logger.info("Request body: {request}", request=request_json)
    try:
        if request_json != {}:
            payload = CurrencyRequestValidation.parse_obj(request_json)
            return CurrencyUpdater.apply_operation(payload)
        return CurrencyUpdater.insert_currency_data()
    except Exception as e:
        logger.error("Error while updating currency data: {error}", error=e)
        return f"Error in currency updater"
    