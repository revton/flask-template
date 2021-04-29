"""User.email required

Revision ID: c3b50ef21e53
Revises: 04423425eafa
Create Date: 2021-04-28 21:18:51.405360

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c3b50ef21e53"
down_revision = "04423425eafa"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.alter_column(
            "email", existing_type=sa.VARCHAR(), nullable=False
        )
        batch_op.create_unique_constraint(
            batch_op.f("uq_user_email"), ["email"]
        )
        batch_op.create_unique_constraint(batch_op.f("uq_user_name"), ["name"])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f("uq_user_name"), type_="unique")
        batch_op.drop_constraint(batch_op.f("uq_user_email"), type_="unique")
        batch_op.alter_column(
            "email", existing_type=sa.VARCHAR(), nullable=True
        )

    # ### end Alembic commands ###
