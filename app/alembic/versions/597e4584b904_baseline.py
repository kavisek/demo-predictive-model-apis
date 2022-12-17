"""baseline

Revision ID: 597e4584b904
Revises: 
Create Date: 2022-12-16 23:32:42.370987

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import JSONB

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
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("variables", JSONB, nullable=False, comment="Variables"),
        sa.Column("prediction", sa.String(255)),
        # sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
        # sa.Column("updated_at", sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table("prediction", if_exists=True)

    op.execute('drop extension if exists "pg_stat_statements"')
    op.execute('drop extension if exists "uuid-ossp"')
# 