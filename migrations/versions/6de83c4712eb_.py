"""empty message

Revision ID: 6de83c4712eb
Revises: f3de3f7d8ede
Create Date: 2022-01-07 19:59:22.677996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6de83c4712eb'
down_revision = 'f3de3f7d8ede'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=64), nullable=True),
    sa.Column('product_link', sa.String(length=120), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('product_link')
    )
    op.create_table('price',
    sa.Column('actual_price', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('change_date', sa.DateTime(), nullable=True),
    sa.Column('change_price', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('actual_price')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('price')
    op.drop_table('product')
    # ### end Alembic commands ###
