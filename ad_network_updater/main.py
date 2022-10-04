from loguru import logger
from src import AdNetworkUpdater, AdNetworktValidation

def http_ad_network_updater(request):
    request_json = request.get_json()
    logger.info("Request body: {request}", request=request_json)
    try:
        return AdNetworkUpdater.insert_data()
    except Exception as e:
        logger.error("Error while updating ad_network data: {error}", error=e)
        return f"Error in ad_network updater"
    