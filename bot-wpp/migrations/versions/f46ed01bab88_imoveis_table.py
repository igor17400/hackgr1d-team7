"""imoveis table

Revision ID: f46ed01bab88
Revises: fd79d071a9ec
Create Date: 2020-04-18 23:12:20.615736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f46ed01bab88'
down_revision = 'fd79d071a9ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('imovel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cep', sa.String(length=120), nullable=True),
    sa.Column('tipo_imovel', sa.String(length=120), nullable=True),
    sa.Column('num_casa', sa.String(length=120), nullable=True),
    sa.Column('valor', sa.String(length=120), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_imovel_cep'), 'imovel', ['cep'], unique=False)
    op.create_index(op.f('ix_imovel_num_casa'), 'imovel', ['num_casa'], unique=False)
    op.create_index(op.f('ix_imovel_timestamp'), 'imovel', ['timestamp'], unique=False)
    op.create_index(op.f('ix_imovel_tipo_imovel'), 'imovel', ['tipo_imovel'], unique=False)
    op.create_index(op.f('ix_imovel_valor'), 'imovel', ['valor'], unique=False)
    op.drop_index('ix_chat_stage_estagio_usuario', table_name='chat_stage')
    op.create_index(op.f('ix_chat_stage_estagio_usuario'), 'chat_stage', ['estagio_usuario'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_chat_stage_estagio_usuario'), table_name='chat_stage')
    op.create_index('ix_chat_stage_estagio_usuario', 'chat_stage', ['estagio_usuario'], unique=1)
    op.drop_index(op.f('ix_imovel_valor'), table_name='imovel')
    op.drop_index(op.f('ix_imovel_tipo_imovel'), table_name='imovel')
    op.drop_index(op.f('ix_imovel_timestamp'), table_name='imovel')
    op.drop_index(op.f('ix_imovel_num_casa'), table_name='imovel')
    op.drop_index(op.f('ix_imovel_cep'), table_name='imovel')
    op.drop_table('imovel')
    # ### end Alembic commands ###
