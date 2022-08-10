"""add content column to posts table

Revision ID: 35683d209e87
Revises: 32dbdfede895
Create Date: 2022-08-10 14:20:22.877739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35683d209e87'
down_revision = '32dbdfede895'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
