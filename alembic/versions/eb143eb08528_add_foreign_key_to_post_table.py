"""add foreign key to post table

Revision ID: eb143eb08528
Revises: 800d98edb1b0
Create Date: 2024-06-16 20:20:27.337913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb143eb08528'
down_revision: Union[str, None] = '800d98edb1b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",
                  sa.Column("user_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users",
                          local_cols=["user_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "user_id")
    
