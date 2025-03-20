"""Initial migration

Revision ID: 87678d8cd782
Revises: 
Create Date: 2025-03-20 02:19:50.118727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87678d8cd782'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=100), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(precision=10, asdecimal=2), nullable=False),
    sa.Column('stock_quantity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###
