"""add user table

Revision ID: 800d98edb1b0
Revises: 1b5b7d984889
Create Date: 2024-06-16 20:06:18.669068

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '800d98edb1b0'
down_revision: Union[str, None] = '1b5b7d984889'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), 
                              nullable=False, server_default=sa.text("now()")),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")                    
                    )


def downgrade() -> None:
    op.drop_table("users")
