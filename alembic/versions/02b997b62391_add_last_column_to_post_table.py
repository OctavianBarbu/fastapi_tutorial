"""add last column to post table

Revision ID: 02b997b62391
Revises: eb143eb08528
Create Date: 2024-06-16 20:26:16.986359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02b997b62391'
down_revision: Union[str, None] = 'eb143eb08528'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",
                  sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", 
                  sa.Column("created_at", sa.TIMESTAMP(timezone=True), 
                            nullable=False, server_default=sa.text("NOW()")))


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
