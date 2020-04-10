"""please

Revision ID: 7fa35b0e4d6f
Revises: 508806fac224
Create Date: 2020-04-10 09:17:27.848374

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "7fa35b0e4d6f"
down_revision = "508806fac224"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "books",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(30), nullable=True),
        sa.Column("author", sa.String(30), nullable=True),
        sa.Column("pages", sa.Integer(), nullable=True),
        sa.Column("published", sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "authentications",
        sa.Column(
            "id",
            mysql.INTEGER(display_width=11),
            server_default=sa.text("'0'"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("user_id", mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
        sa.Column("category", mysql.VARCHAR(length=45), nullable=False),
        sa.Column("identification", mysql.VARCHAR(length=45), nullable=False),
        sa.Column("secret", mysql.VARCHAR(length=45), nullable=False),
        sa.Column(
            "created_at",
            mysql.DATETIME(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            mysql.DATETIME(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_default_charset="utf8",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "users",
        sa.Column(
            "id", mysql.INTEGER(display_width=11), autoincrement=True, nullable=False, comment="id"
        ),
        sa.Column("nickname", mysql.VARCHAR(length=45), nullable=False, comment="닉네임"),
        sa.Column("birthday", mysql.VARCHAR(length=45), nullable=False, comment="생년월일"),
        sa.Column(
            "created_at",
            mysql.DATETIME(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
            comment="생성시간",
        ),
        sa.Column(
            "updated_at",
            mysql.DATETIME(),
            server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            nullable=False,
            comment="업뎃시간",
        ),
        sa.PrimaryKeyConstraint("id"),
        comment="유저 정보",
        mysql_comment="유저 정보",
        mysql_default_charset="utf8",
        mysql_engine="InnoDB",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "authentications",
        sa.Column(
            "id",
            mysql.INTEGER(display_width=11),
            server_default=sa.text("'0'"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("user_id", mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
        sa.Column("category", mysql.VARCHAR(length=45), nullable=False),
        sa.Column("identification", mysql.VARCHAR(length=45), nullable=False),
        sa.Column("secret", mysql.VARCHAR(length=45), nullable=False),
        sa.Column(
            "created_at",
            mysql.DATETIME(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            mysql.DATETIME(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_default_charset="utf8",
        mysql_engine="InnoDB",
    )
    op.create_table(
        "users",
        sa.Column(
            "id", mysql.INTEGER(display_width=11), autoincrement=True, nullable=False, comment="id"
        ),
        sa.Column("nickname", mysql.VARCHAR(length=45), nullable=False, comment="닉네임"),
        sa.Column("birthday", mysql.VARCHAR(length=45), nullable=False, comment="생년월일"),
        sa.Column(
            "created_at",
            mysql.DATETIME(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
            comment="생성시간",
        ),
        sa.Column(
            "updated_at",
            mysql.DATETIME(),
            server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            nullable=False,
            comment="업뎃시간",
        ),
        sa.PrimaryKeyConstraint("id"),
        comment="유저 정보",
        mysql_comment="유저 정보",
        mysql_default_charset="utf8",
        mysql_engine="InnoDB",
    )
    op.drop_table("books")
    # ### end Alembic commands ###
