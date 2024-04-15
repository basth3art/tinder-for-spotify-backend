"""empty message

Revision ID: d20a5048716c
Revises: 50e2127cb63b
Create Date: 2024-04-15 11:20:32.508876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd20a5048716c'
down_revision = '50e2127cb63b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users-top-artists',
    sa.Column('id', sa.String(length=15), nullable=False),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('artist_id', sa.String(), nullable=True),
    sa.Column('position_for_user', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users-top-artists', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users-top-artists_artist_id'), ['artist_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_users-top-artists_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users-top-artists', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users-top-artists_user_id'))
        batch_op.drop_index(batch_op.f('ix_users-top-artists_artist_id'))

    op.drop_table('users-top-artists')
    op.drop_table('artists')
    # ### end Alembic commands ###