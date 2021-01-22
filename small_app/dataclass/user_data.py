from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator


class UserConfigData(BaseModel):
    email: str
    password: str
    driver: str
    waiting_seconds: Optional[int] = 15

    @validator("driver")
    def is_driver_in_list(self, value: str):
        basic_driver = ["chrome", "firefox"]
        if value not in basic_driver:
            raise ValueError("지원하지 않는 드라이버")
        return value
