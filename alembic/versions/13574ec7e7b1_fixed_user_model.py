"""fixed user model

Revision ID: 13574ec7e7b1
Revises: cc452ad3702c
Create Date: 2024-06-21 22:24:08.593758

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13574ec7e7b1'
down_revision: Union[str, None] = 'cc452ad3702c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username', server_default="Unnamed")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username', server_default=None)
    # ### end Alembic commands ###

