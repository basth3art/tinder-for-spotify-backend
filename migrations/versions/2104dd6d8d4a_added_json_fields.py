"""Added json fields

Revision ID: 2104dd6d8d4a
Revises: b4018b4001a0
Create Date: 2024-06-06 19:22:53.351031

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2104dd6d8d4a'
down_revision = 'b4018b4001a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users-top-tracks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tracks', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
        batch_op.add_column(sa.Column('next_update', sa.DateTime(), nullable=True))
        batch_op.drop_index('ix_users-top-tracks_track_id')
        batch_op.drop_constraint('users-top-tracks_track_id_fkey', type_='foreignkey')
        batch_op.drop_column('position_for_user')
        batch_op.drop_column('created_at')
        batch_op.drop_column('track_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users-top-tracks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('track_id', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('position_for_user', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('users-top-tracks_track_id_fkey', 'tracks', ['track_id'], ['id'])
        batch_op.create_index('ix_users-top-tracks_track_id', ['track_id'], unique=False)
        batch_op.drop_column('next_update')
        batch_op.drop_column('tracks')

    # ### end Alembic commands ###
