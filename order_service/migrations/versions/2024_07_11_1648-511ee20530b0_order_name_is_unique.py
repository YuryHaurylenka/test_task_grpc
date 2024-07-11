"""order_name is unique


Revision ID: 511ee20530b0
Revises: a73a3d2a352a
Create Date: 2024-07-11 16:48:36.766171

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '511ee20530b0'
down_revision: Union[str, None] = 'a73a3d2a352a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'orders', ['order_name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'orders', type_='unique')
    # ### end Alembic commands ###
