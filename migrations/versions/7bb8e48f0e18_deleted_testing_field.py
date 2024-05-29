"""deleted testing field

Revision ID: 7bb8e48f0e18
Revises: 61b821cc0467
Create Date: 2024-05-18 18:16:33.544426

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7bb8e48f0e18"
down_revision = "61b821cc0467"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_column("new_shit")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "new_shit", sa.VARCHAR(length=50), autoincrement=False, nullable=True
            )
        )

    # ### end Alembic commands ###
