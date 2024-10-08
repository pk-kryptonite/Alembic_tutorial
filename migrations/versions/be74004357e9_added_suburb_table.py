"""Added suburb table

Revision ID: be74004357e9
Revises: bbf10cb609c5
Create Date: 2024-09-10 15:58:47.406773

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be74004357e9'
down_revision: Union[str, None] = 'bbf10cb609c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('suburbs',
    sa.Column('uuid', sa.String(length=40), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('street_code_uuid', sa.String(length=40), nullable=True),
    sa.Column('postal_code_uuid', sa.String(length=40), nullable=True),
    sa.Column('town_uuid', sa.String(length=40), nullable=True),
    sa.Column('municipality_uuid', sa.String(length=40), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('suburbs')
    # ### end Alembic commands ###
