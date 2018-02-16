"""empty message

Revision ID: 008580c0fae1
Revises: 917a157ad6ca
Create Date: 2018-02-12 19:35:00.882582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '008580c0fae1'
down_revision = '917a157ad6ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('tele', sa.String(length=128), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('tele', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.drop_table('test')
    # ### end Alembic commands ###