"""Chapter-course

Revision ID: d68ab6cb47bb
Revises: bbda39c0a8cb
Create Date: 2023-04-08 18:08:25.704375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd68ab6cb47bb'
down_revision = 'bbda39c0a8cb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chapters', sa.Column('course_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'chapters', 'courses', ['course_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'chapters', type_='foreignkey')
    op.drop_column('chapters', 'course_id')
    # ### end Alembic commands ###
