from typing import Optional, Dict
from pydantic import BaseModel, Field

class CurrencyRequestValidation(BaseModel):
    operation_type: str = Field(alias="operation")
    start_date: str = Field(alias="startDate")
    end_date: str = Field(alias="endDate")