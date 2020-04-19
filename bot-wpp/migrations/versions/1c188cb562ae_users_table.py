"""users table

Revision ID: 1c188cb562ae
Revises: cf4799b27c71
Create Date: 2020-04-18 20:53:30.071085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c188cb562ae'
down_revision = 'cf4799b27c71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_chat_stage_estagio_usuario', table_name='chat_stage')
    op.create_index(op.f('ix_chat_stage_estagio_usuario'), 'chat_stage', ['estagio_usuario'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_chat_stage_estagio_usuario'), table_name='chat_stage')
    op.create_index('ix_chat_stage_estagio_usuario', 'chat_stage', ['estagio_usuario'], unique=1)
    # ### end Alembic commands ###
