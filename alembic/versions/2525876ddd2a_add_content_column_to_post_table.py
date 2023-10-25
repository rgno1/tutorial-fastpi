"""add content column to post table

Revision ID: 2525876ddd2a
Revises: 75b9eec8895c
Create Date: 2023-10-24 09:14:14.898746

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2525876ddd2a'
down_revision: Union[str, None] = '75b9eec8895c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts', 
        sa.Column('content', sa.String(), nullable=False)
        )
    pass


def downgrade() -> None:

    op.drop_column('post','content')
    pass
