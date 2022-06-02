"""empty message

Revision ID: d4dc74b1277a
Revises: 4032a6c2009c
Create Date: 2022-06-02 02:15:31.520530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4dc74b1277a'
down_revision = '4032a6c2009c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('company_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'jobs', 'companies', ['company_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'jobs', type_='foreignkey')
    op.drop_column('jobs', 'company_id')
    # ### end Alembic commands ###
