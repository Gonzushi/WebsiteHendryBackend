"""empty message

Revision ID: 1c34b6fdcd2c
Revises: 60ef4eabd24f
Create Date: 2024-04-25 19:51:38.048459

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c34b6fdcd2c'
down_revision: Union[str, None] = '60ef4eabd24f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
