"""Chapter

Revision ID: bbda39c0a8cb
Revises: 951d6445c4f8
Create Date: 2023-04-08 18:05:34.083696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbda39c0a8cb'
down_revision = '951d6445c4f8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chapters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.Column('percentage', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_chapters_id'), 'chapters', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_chapters_id'), table_name='chapters')
    op.drop_table('chapters')
    # ### end Alembic commands ###
