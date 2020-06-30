"""empty message

Revision ID: c5e89c70e54e
Revises: 
Create Date: 2020-06-29 14:31:28.079665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5e89c70e54e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sem_cal_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('_password', sa.String(length=256), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('permissiomn', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sem_cal_user')
    # ### end Alembic commands ###