"""empty message

Revision ID: 36e5daa6f29b
Revises: d7e5f3ec4b5a
Create Date: 2022-05-31 17:40:58.192351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36e5daa6f29b'
down_revision = 'd7e5f3ec4b5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('profiles', 'avator',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('profiles', 'resume',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('profiles', 'resume',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('profiles', 'avator',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    # ### end Alembic commands ###