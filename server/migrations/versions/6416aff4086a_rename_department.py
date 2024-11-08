"""rename department

Revision ID: 6416aff4086a
Revises: b9daed753fcd
Create Date: 2024-11-07 17:32:40.028709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6416aff4086a'
down_revision = 'b9daed753fcd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('name', sa.String(), nullable=False),
    # sa.Column('address', sa.String(), nullable=True),
    # sa.PrimaryKeyConstraint('id')
    # )
    # op.drop_table('department')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # sa.Column('id', sa.INTEGER(), nullable=False),
    # sa.Column('name', sa.VARCHAR(), nullable=False),
    # sa.Column('address', sa.VARCHAR(), nullable=True),
    # sa.PrimaryKeyConstraint('id')
    # )
    # op.drop_table('departments')
    # ### end Alembic commands ###