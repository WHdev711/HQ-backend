"""empty message

Revision ID: eee4afeeab06
Revises: aee50b049219
Create Date: 2022-05-31 17:29:31.538059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eee4afeeab06'
down_revision = 'aee50b049219'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('video_id', sa.Integer(), nullable=True))
    op.add_column('profiles', sa.Column('user_id', sa.Integer(), nullable=False))
    op.add_column('profiles', sa.Column('job_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'profiles', 'jobs', ['job_id'], ['id'])
    op.create_foreign_key(None, 'profiles', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'profiles', 'videos', ['video_id'], ['id'])
    op.drop_column('profiles', 'video')
    op.drop_column('profiles', 'target_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('target_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('video', sa.VARCHAR(length=128), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'profiles', type_='foreignkey')
    op.drop_constraint(None, 'profiles', type_='foreignkey')
    op.drop_constraint(None, 'profiles', type_='foreignkey')
    op.drop_column('profiles', 'job_id')
    op.drop_column('profiles', 'user_id')
    op.drop_column('profiles', 'video_id')
    # ### end Alembic commands ###
