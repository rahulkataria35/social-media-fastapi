"""add last fews to posts table

Revision ID: bf98856cb036
Revises: 30594b2cb7da
Create Date: 2024-02-09 00:11:39.227473

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf98856cb036'
down_revision: Union[str, None] = '30594b2cb7da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default='TRUE')
    )
    op.add_column(
        "posts",
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()"))
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
