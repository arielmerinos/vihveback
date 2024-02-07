"""Add username column to users table

Revision ID: 46b66a334f77
Revises: 41d330303c20
Create Date: 2024-02-06 15:41:34.308218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46b66a334f77'
down_revision: Union[str, None] = '41d330303c20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_rooms_id', table_name='rooms')
    op.drop_index('ix_rooms_name', table_name='rooms')
    op.drop_table('rooms')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rooms',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='rooms_pkey')
    )
    op.create_index('ix_rooms_name', 'rooms', ['name'], unique=False)
    op.create_index('ix_rooms_id', 'rooms', ['id'], unique=False)
    # ### end Alembic commands ###
