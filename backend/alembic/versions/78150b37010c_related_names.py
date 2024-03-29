"""related names

Revision ID: 78150b37010c
Revises: b132fe31c91a
Create Date: 2024-03-18 23:13:59.662409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78150b37010c'
down_revision = 'b132fe31c91a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book_users', sa.Column('books_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book_users', 'books_count')
    # ### end Alembic commands ###
