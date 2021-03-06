"""seguro_familia table

Revision ID: 0e871e1321c1
Revises: f46ed01bab88
Create Date: 2020-04-19 17:08:09.416023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e871e1321c1'
down_revision = 'f46ed01bab88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('seguro_familia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_nascimento', sa.String(length=120), nullable=True),
    sa.Column('sexo', sa.String(length=120), nullable=True),
    sa.Column('cep', sa.String(length=180), nullable=True),
    sa.Column('problema_de_saude', sa.String(length=180), nullable=True),
    sa.Column('doencas', sa.String(length=180), nullable=True),
    sa.Column('deficiencia', sa.String(length=180), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_seguro_familia_cep'), 'seguro_familia', ['cep'], unique=False)
    op.create_index(op.f('ix_seguro_familia_data_nascimento'), 'seguro_familia', ['data_nascimento'], unique=False)
    op.create_index(op.f('ix_seguro_familia_deficiencia'), 'seguro_familia', ['deficiencia'], unique=False)
    op.create_index(op.f('ix_seguro_familia_doencas'), 'seguro_familia', ['doencas'], unique=False)
    op.create_index(op.f('ix_seguro_familia_problema_de_saude'), 'seguro_familia', ['problema_de_saude'], unique=False)
    op.create_index(op.f('ix_seguro_familia_sexo'), 'seguro_familia', ['sexo'], unique=False)
    op.create_index(op.f('ix_seguro_familia_timestamp'), 'seguro_familia', ['timestamp'], unique=False)
    op.add_column('imovel', sa.Column('renda', sa.String(length=120), nullable=True))
    op.create_index(op.f('ix_imovel_renda'), 'imovel', ['renda'], unique=False)
    op.drop_index('ix_user_username', table_name='user')
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.create_index('ix_user_username', 'user', ['username'], unique=1)
    op.drop_index(op.f('ix_imovel_renda'), table_name='imovel')
    op.drop_column('imovel', 'renda')
    op.drop_index(op.f('ix_seguro_familia_timestamp'), table_name='seguro_familia')
    op.drop_index(op.f('ix_seguro_familia_sexo'), table_name='seguro_familia')
    op.drop_index(op.f('ix_seguro_familia_problema_de_saude'), table_name='seguro_familia')
    op.drop_index(op.f('ix_seguro_familia_doencas'), table_name='seguro_familia')
    op.drop_index(op.f('ix_seguro_familia_deficiencia'), table_name='seguro_familia')
    op.drop_index(op.f('ix_seguro_familia_data_nascimento'), table_name='seguro_familia')
    op.drop_index(op.f('ix_seguro_familia_cep'), table_name='seguro_familia')
    op.drop_table('seguro_familia')
    # ### end Alembic commands ###
