"""add content column to post table

Revision ID: 1b5b7d984889
Revises: 9d5f948ba163
Create Date: 2024-06-16 20:00:16.826642

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b5b7d984889'
down_revision: Union[str, None] = '9d5f948ba163'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
