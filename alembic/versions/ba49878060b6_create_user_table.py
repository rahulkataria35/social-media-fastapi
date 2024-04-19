"""create user table

Revision ID: ba49878060b6
Revises: 0313c6f8c56d
Create Date: 2024-02-08 23:43:08.852264

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer, Column, String, TIMESTAMP



# revision identifiers, used by Alembic.
revision: str = 'ba49878060b6'
down_revision: Union[str, None] = '0313c6f8c56d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "users",
        Column('id', Integer, nullable=False),
        Column('email', String, nullable=False),
        Column('password', String, nullable=False),
        Column('created_at', TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint("email")
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
