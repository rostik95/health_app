"""created weight table and relationship to user table

Revision ID: a20316c4961a
Revises: 2b721a458b06
Create Date: 2024-05-21 15:05:08.439731

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a20316c4961a"
down_revision = "2b721a458b06"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "weight",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("value_in_kg", sa.Float(), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.add_column(sa.Column("height_in_cm", sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_column("height_in_cm")

    op.drop_table("weight")
    # ### end Alembic commands ###
