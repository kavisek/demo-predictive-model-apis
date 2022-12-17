from pydantic import BaseModel
from typing import List, Optional


class PredictionBase(BaseModel):
    variables: dict

    class Config:
        orm_mode = True