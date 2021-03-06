"""empty message

Revision ID: 917a157ad6ca
Revises: 
Create Date: 2018-02-01 20:45:01.195627

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '917a157ad6ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('tele', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('schemaversion')
    op.drop_table('users')
    op.drop_table('users_teams')
    op.drop_table('teams')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teams',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('createdAt', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('updatedAt', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='teams_pkey')
    )
    op.create_table('users_teams',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('team_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('createdAt', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('updatedAt', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('is_current', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('role', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_teams_pkey')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('admin', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('password_digest', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('photo_url', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('slack_handle', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('nickname', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('location', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('manager_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('about_me', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('interests', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='uc_email')
    )
    op.create_table('schemaversion',
    sa.Column('version', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('name', sa.TEXT(), server_default=sa.text("''::text"), autoincrement=False, nullable=True),
    sa.Column('md5', sa.TEXT(), server_default=sa.text("''::text"), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('version', name='schemaversion_pkey')
    )
    op.drop_table('user')
    # ### end Alembic commands ###
