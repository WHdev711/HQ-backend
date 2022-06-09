"""empty message

Revision ID: 4e43c96bb85d
Revises: 6cc2cdb1c1bb
Create Date: 2022-06-09 19:13:07.808321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e43c96bb85d'
down_revision = '6cc2cdb1c1bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appliedjobs', sa.Column('shortlist_status', sa.Boolean(), nullable=True))
    op.add_column('appliedjobs', sa.Column('shortlist_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('appliedjobs', 'shortlist_at')
    op.drop_column('appliedjobs', 'shortlist_status')
    # ### end Alembic commands ###
