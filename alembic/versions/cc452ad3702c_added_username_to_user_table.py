"""added username to user table

Revision ID: cc452ad3702c
Revises: f455f8864ce3
Create Date: 2024-06-20 21:23:25.628777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc452ad3702c'
down_revision: Union[str, None] = 'f455f8864ce3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('username', sa.String(), nullable=False, default="Unnamed"))


def downgrade() -> None:
    op.drop_column('users', 'username')

