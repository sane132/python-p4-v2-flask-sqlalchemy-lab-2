"""Initial tables

Revision ID: 229ea0a76e25
Revises: 
Create Date: 2025-09-20 12:18:38.712057
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '229ea0a76e25'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create customers table
    op.create_table(
        'customers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
    )

    # Create items table
    op.create_table(
        'items',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
    )

    # Create reviews table
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('comment', sa.String(), nullable=False),
        sa.Column('customer_id', sa.Integer(), sa.ForeignKey('customers.id'), nullable=False),
        sa.Column('item_id', sa.Integer(), sa.ForeignKey('items.id'), nullable=False),
    )


def downgrade():
    op.drop_table('reviews')
    op.drop_table('items')
    op.drop_table('customers')
