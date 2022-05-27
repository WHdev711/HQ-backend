"""empty message

Revision ID: 8c5b50f94d0f
Revises: 969a287e3ba1
Create Date: 2022-05-27 05:42:00.800936

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8c5b50f94d0f'
down_revision = '969a287e3ba1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('description', sa.String(length=128), nullable=False),
    sa.Column('post_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('status', sa.String(length=128), nullable=False),
    sa.Column('candidates', postgresql.ARRAY(sa.String(length=128)), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Jobs')
    # ### end Alembic commands ###
