import uuid 
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db import Base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy_utils import UUIDType
import pendulum

# Models contains the ORM models for the database tables. These models are used to
# represent the data in the database. Schema migration is handled by Alembic.
# https://alembic.sqlalchemy.org/en/latest/tutorial.html
# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-sqlalchemy-orm-models

class Predictions(Base):
    __tablename__ = "predictions"

    id = sa.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    user_id = sa.Column(sa.Integer, nullable=False)
    variables = sa.Column(JSONB, nullable=False)
    prediction = sa.Column(sa.String(255))
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now(), nullable=False)
    updated_at = sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)

    def __repr__(self):
        id = str(self.id)
        user_id = self.user_id
        print(self.variables)
        variables = eval(self.variables)
        prediction = self.prediction
        return f"Prediction(id={id}, user_id={user_id}, variables={variables}, prediction={prediction})"