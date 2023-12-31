"""Image attribute added to property class

Revision ID: 164783e8c2de
Revises: 843649122f52
Create Date: 2023-07-04 12:50:25.035658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '164783e8c2de'
down_revision = '843649122f52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###
