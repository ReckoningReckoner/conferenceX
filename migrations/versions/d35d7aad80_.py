"""empty message

Revision ID: d35d7aad80
Revises: 3dc6ff9d729
Create Date: 2016-06-30 10:50:18.449657

"""

# revision identifiers, used by Alembic.
revision = 'd35d7aad80'
down_revision = '3dc6ff9d729'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('HTML', sa.Column('sponsor_url', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('HTML', 'sponsor_url')
    ### end Alembic commands ###
