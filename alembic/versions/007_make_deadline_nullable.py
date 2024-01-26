"""make_deadline_nullable

Revision ID: 007
Revises: 006
Create Date: 2024-01-28 03:08:53.573541

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '007'
down_revision: Union[str, None] = '006'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pdp', 'deadline',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('task', 'deadline',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'deadline',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('pdp', 'deadline',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###