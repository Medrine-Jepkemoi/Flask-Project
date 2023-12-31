"""Rating table added

Revision ID: 45175f279515
Revises: 61f3e8f8b96d
Create Date: 2023-07-04 22:40:12.646258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45175f279515'
down_revision = '61f3e8f8b96d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ratings',
    sa.Column('rating_id', sa.Integer(), nullable=False),
    sa.Column('property_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['property_id'], ['properties.property_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('rating_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ratings')
    # ### end Alembic commands ###
