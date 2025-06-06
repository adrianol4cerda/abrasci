"""users full_name

Revision ID: fb859d6fc3ba
Revises: bf6ed4acf2c1
Create Date: 2024-11-01 14:37:45.019805

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb859d6fc3ba'
down_revision: Union[str, None] = 'bf6ed4acf2c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('full_name', sa.String(), nullable=False))
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('user', 'full_name')
    # ### end Alembic commands ###
