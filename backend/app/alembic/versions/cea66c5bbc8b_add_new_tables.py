"""Add new tables

Revision ID: cea66c5bbc8b
Revises: d4867f3a4c0a
Create Date: 2020-03-25 13:24:34.952420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cea66c5bbc8b'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('field',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('value', sa.JSON(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_field_id'), 'field', ['id'], unique=False)
    op.create_index(op.f('ix_field_name'), 'field', ['name'], unique=True)
    op.create_table('status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_status_id'), 'status', ['id'], unique=False)
    op.create_index(op.f('ix_status_name'), 'status', ['name'], unique=True)
    op.create_index(op.f('ix_status_value'), 'status', ['value'], unique=True)
    op.create_table('response',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['status_id'], ['status.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_response_id'), 'response', ['id'], unique=False)
    op.create_index(op.f('ix_response_name'), 'response', ['name'], unique=True)
    op.create_table('action',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('data', sa.JSON(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('response_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['response_id'], ['response.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_action_description'), 'action', ['description'], unique=False)
    op.create_index(op.f('ix_action_id'), 'action', ['id'], unique=False)
    op.create_index(op.f('ix_action_name'), 'action', ['name'], unique=True)
    op.create_table('responsefield',
    sa.Column('response_id', sa.Integer(), nullable=False),
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['field_id'], ['field.id'], ),
    sa.ForeignKeyConstraint(['response_id'], ['response.id'], ),
    sa.PrimaryKeyConstraint('response_id', 'field_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('responsefield')
    op.drop_index(op.f('ix_action_name'), table_name='action')
    op.drop_index(op.f('ix_action_id'), table_name='action')
    op.drop_index(op.f('ix_action_description'), table_name='action')
    op.drop_table('action')
    op.drop_index(op.f('ix_response_name'), table_name='response')
    op.drop_index(op.f('ix_response_id'), table_name='response')
    op.drop_table('response')
    op.drop_index(op.f('ix_status_value'), table_name='status')
    op.drop_index(op.f('ix_status_name'), table_name='status')
    op.drop_index(op.f('ix_status_id'), table_name='status')
    op.drop_table('status')
    op.drop_index(op.f('ix_field_name'), table_name='field')
    op.drop_index(op.f('ix_field_id'), table_name='field')
    op.drop_table('field')
    # ### end Alembic commands ###
