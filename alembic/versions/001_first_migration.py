"""First migration

Revision ID: 001
Revises: 
Create Date: 2024-01-20 02:27:02.644086

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "status",
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column(
            "role",
            sa.Enum("CHIEF", "EMPLOYEE", name="userrole"),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "type",
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "user",
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("first_name", sa.String(length=150), nullable=False),
        sa.Column("last_name", sa.String(length=150), nullable=False),
        sa.Column("patronymic_name", sa.String(length=150), nullable=True),
        sa.Column("position", sa.String(length=150), nullable=False),
        sa.Column(
            "role",
            sa.Enum("CHIEF", "EMPLOYEE", name="userrole"),
            nullable=False,
        ),
        sa.Column("photo", sa.String(length=200), nullable=True),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_table(
        "pdp",
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("goal", sa.String(length=100), nullable=False),
        sa.Column("starting_date", sa.Date(), nullable=True),
        sa.Column("deadline", sa.Date(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_user",
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("chief_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["chief_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
    )
    op.create_table(
        "task",
        sa.Column("pdp_id", sa.Integer(), nullable=True),
        sa.Column("type", sa.Integer(), nullable=True),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("skills", sa.String(length=100), nullable=False),
        sa.Column("chief_comment", sa.Text(), nullable=True),
        sa.Column("employee_comment", sa.Text(), nullable=True),
        sa.Column("status", sa.Integer(), nullable=True),
        sa.Column("starting_date", sa.Date(), nullable=True),
        sa.Column("deadline", sa.Date(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["pdp_id"],
            ["pdp.id"],
        ),
        sa.ForeignKeyConstraint(
            ["status"],
            ["status.id"],
        ),
        sa.ForeignKeyConstraint(
            ["type"],
            ["type.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("task")
    op.drop_table("user_user")
    op.drop_table("pdp")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    op.drop_table("type")
    op.drop_table("status")
    # ### end Alembic commands ###
