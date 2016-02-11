"""Dropping Workers and new Jobs

Revision ID: 4bbcb4d706ef
Revises: 28015a6e5b8
Create Date: 2015-02-06 18:02:02.215441

"""

# revision identifiers, used by Alembic.
revision = '4bbcb4d706ef'
down_revision = '28015a6e5b8'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.add_column(sa.Column('settings', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('type', sa.String(length=64), nullable=True))
        batch_op.drop_column('format')
        batch_op.drop_column('frame_end')
        batch_op.drop_column('filepath')
        batch_op.drop_column('render_settings')
        batch_op.drop_column('chunk_size')
        batch_op.drop_column('current_frame')
        batch_op.drop_column('frame_start')

    with op.batch_alter_table('manager', schema=None) as batch_op:
        batch_op.drop_column('total_workers')
        batch_op.drop_column('running_tasks')

    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('activity', sa.String(length=256), nullable=True))
        batch_op.add_column(sa.Column('log', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('name', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('settings', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('type', sa.String(length=64), nullable=True))
        batch_op.drop_column('chunk_end')
        batch_op.drop_column('current_frame')
        batch_op.drop_column('chunk_start')

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('chunk_start', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('current_frame', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('chunk_end', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.drop_column('type')
        batch_op.drop_column('settings')
        batch_op.drop_column('name')
        batch_op.drop_column('log')
        batch_op.drop_column('activity')

    with op.batch_alter_table('manager', schema=None) as batch_op:
        batch_op.add_column(sa.Column('running_tasks', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('total_workers', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))

    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.add_column(sa.Column('frame_start', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('current_frame', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('chunk_size', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('render_settings', mysql.VARCHAR(length=120), nullable=True))
        batch_op.add_column(sa.Column('filepath', mysql.VARCHAR(length=256), nullable=True))
        batch_op.add_column(sa.Column('frame_end', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('format', mysql.VARCHAR(length=10), nullable=True))
        batch_op.drop_column('type')
        batch_op.drop_column('settings')

    ### end Alembic commands ###
