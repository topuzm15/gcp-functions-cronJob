import os
from datetime import datetime, timedelta

class EtlConfig:
    currency_base = os.getenv("CURRENCY_BASE", "USD")
    day_gap = int(os.getenv("DAY_GAP", "250"))
    min_date = (datetime.today() - timedelta(days=day_gap)).strftime("%Y-%m-%d")
    
