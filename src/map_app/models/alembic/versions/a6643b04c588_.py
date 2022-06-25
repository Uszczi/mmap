"""empty message

Revision ID: a6643b04c588
Revises: cca091187b78
Create Date: 2022-06-25 12:28:23.824951

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a6643b04c588"
down_revision = "cca091187b78"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("routes", sa.Column("activity", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("routes", "activity")
    # ### end Alembic commands ###
