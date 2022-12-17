"""baseline

Revision ID: 597e4584b904
Revises: 
Create Date: 2022-12-16 23:32:42.370987

"""
from alembic import op
import sqlalchemy as sa

import uuid
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy_utils import UUIDType

# revision identifiers, used by Alembic.
revision = '597e4584b904'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass

    # creating a prediction table
    
    op.execute('create extension if not exists "uuid-ossp"')
    op.execute('create extension if not exists "pg_stat_statements"')

    # drop table if exists
    op.execute('drop table if exists predictions')
    op.create_table(
        "predictions",
        sa.Column("id", UUIDType(binary=False), primary_key=True, default=uuid.uuid4),
        sa.Column("user_id", sa.Integer, nullable=False),
        sa.Column("variables", JSONB, nullable=False),
        sa.Column("prediction", sa.String(255)),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("prediction", if_exists=True)

    op.execute('drop extension if exists "pg_stat_statements"')
    op.execute('drop extension if exists "uuid-ossp"')
# 