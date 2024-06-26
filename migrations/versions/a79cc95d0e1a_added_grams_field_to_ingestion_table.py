"""added grams field to ingestion table

Revision ID: a79cc95d0e1a
Revises: e68ee3db7080
Create Date: 2024-05-29 11:08:39.688808

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a79cc95d0e1a"
down_revision = "e68ee3db7080"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("ingestion", schema=None) as batch_op:
        batch_op.add_column(sa.Column("grams", sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("ingestion", schema=None) as batch_op:
        batch_op.drop_column("grams")

    # ### end Alembic commands ###
