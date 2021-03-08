"""formapagamento e pedido

Revision ID: 0cb2470bbd48
Revises: 
Create Date: 2021-03-08 11:55:21.327569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cb2470bbd48'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categoria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('descricao', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('endereco',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cep', sa.String(length=100), nullable=False),
    sa.Column('rua', sa.String(length=255), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('casa', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('forma_pagamento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('login', sa.String(length=20), nullable=False),
    sa.Column('senha', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('login')
    )
    op.create_table('agricultor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('endereco_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['endereco_id'], ['endereco.id'], ),
    sa.ForeignKeyConstraint(['id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('preco_total', sa.Float(), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=False),
    sa.Column('forma_pagamento_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['forma_pagamento_id'], ['forma_pagamento.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('produto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('preco', sa.Float(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.Column('agricultor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['agricultor_id'], ['agricultor.id'], ),
    sa.ForeignKeyConstraint(['categoria_id'], ['categoria.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produto')
    op.drop_table('pedido')
    op.drop_table('cliente')
    op.drop_table('agricultor')
    op.drop_table('usuario')
    op.drop_table('forma_pagamento')
    op.drop_table('endereco')
    op.drop_table('categoria')
    # ### end Alembic commands ###
