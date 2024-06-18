"""Created Friends Table

Revision ID: 73687c4128ad
Revises: 2104dd6d8d4a
Create Date: 2024-06-18 11:28:10.386645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73687c4128ad'
down_revision = '2104dd6d8d4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friend-requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=50), nullable=True),
    sa.Column('friend_id', sa.String(length=50), nullable=True),
    sa.Column('status', sa.Enum('pending', 'accepted', 'rejeted', name='friendrequeststatus'), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['friend_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('friend-requests', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_friend-requests_friend_id'), ['friend_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_friend-requests_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('friend-requests', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_friend-requests_user_id'))
        batch_op.drop_index(batch_op.f('ix_friend-requests_friend_id'))

    op.drop_table('friend-requests')
    # ### end Alembic commands ###
