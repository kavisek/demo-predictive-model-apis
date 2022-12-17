from pydantic import BaseModel
from typing import List, Optional

# NOTE: Pydantic model are used to validate the data that is passed to the API.
# There are also use to generate the inputs and outputs of the API documentation.
# If you are using a pydantic model with an ORM. You need to set the Config.orm_mode = True


class PredictionBase(BaseModel):
    id: int
    variables: dict

    class Config:
        orm_mode = True