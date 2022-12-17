# Pydantic prediction model

import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db import Base
from sqlalchemy.dialects.postgresql import JSONB

class Predictions(Base):
    __tablename__ = "predictions"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    variables = sa.Column(JSONB, nullable=False, comment="Variables")
    prediction = sa.Column(sa.String(255))

    def __repr__(self):
        return f"Prediction(id={self.id}, variables={self.variables}, prediction={self.prediction})"