"""empty message

Revision ID: 989218bc8bdc
Revises: d49663785c21
Create Date: 2019-08-09 23:37:04.427169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '989218bc8bdc'
down_revision = 'd49663785c21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('ip_details_ip_address_key', 'ip_details', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('ip_details_ip_address_key', 'ip_details', ['ip_address'])
    # ### end Alembic commands ###
