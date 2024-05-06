"""add foreign-key to posts table

Revision ID: 30594b2cb7da
Revises: ba49878060b6
Create Date: 2024-02-08 23:55:14.128055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30594b2cb7da'
down_revision: Union[str, None] = 'ba49878060b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts", sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key("post_user_fk", source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint("post_user_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
