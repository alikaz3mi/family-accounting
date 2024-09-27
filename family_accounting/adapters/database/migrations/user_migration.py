"""Add first_name, last_name, username, and password to User table

Revision ID: <generated_revision_id>
Revises: <previous_revision_id>
Create Date: <timestamp>
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'create_user_table'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sa.String(length=50), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(length=50), nullable=True))
    op.add_column('users', sa.Column('username', sa.String(length=50), nullable=True))
    op.add_column('users', sa.Column('password', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'password')
    op.drop_column('users', 'username')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###
