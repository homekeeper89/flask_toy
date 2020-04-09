"""first

Revision ID: 508806fac224
Revises: 
Create Date: 2020-04-09 23:09:39.117196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "508806fac224"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "account",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("description", sa.Unicode(200)),
    )


def downgrade():
    pass
