from typing import Optional, Dict
from pydantic import BaseModel, Field

class CurrencyRequestValidation(BaseModel):
    app_language: Optional[str] = Field(alias="appLanguage")
    domain_type: Optional[int] = Field(alias="domainType")
    country_code: Optional[str] = Field(alias="countryCode")
    client_id: Optional[str] = Field(alias="clientId", default = '')
    warehouse_id: Optional[str] = Field(alias="warehouseId", default = '')
    client_location: Optional[Dict[str, float]] = Field(alias="clientLocation")