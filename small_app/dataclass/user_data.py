from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator


class UserConfigData(BaseModel):
    target_url: str
    email: str
    password: str
    driver: str
    waiting_seconds: Optional[int] = 15

    @validator("driver")
    def is_driver_in_list(cls, value: str):
        basic_driver = ["chrome", "firefox"]
        if value not in basic_driver:
            raise ValueError("지원하지 않는 드라이버")
        return value


class FilterData(BaseModel):
    need_words: List[str] = [""]
    ben_words: List[str] = [""]
