"""add content column to posts table

Revision ID: 0313c6f8c56d
Revises: 37592028b277
Create Date: 2024-02-08 23:33:47.887454

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0313c6f8c56d'
down_revision: Union[str, None] = '37592028b277'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
