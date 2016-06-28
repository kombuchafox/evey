"""empty message

Revision ID: 771c476040ed
Revises: 139d0b7c1d8d
Create Date: 2016-06-27 22:08:00.851320

"""

# revision identifiers, used by Alembic.
revision = '771c476040ed'
down_revision = '139d0b7c1d8d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('conversation')
    op.drop_table('message')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('body', sa.TEXT(), nullable=True),
    sa.Column('conversation_id', sa.INTEGER(), nullable=True),
    sa.Column('message_uid', sa.VARCHAR(), nullable=True),
    sa.Column('time', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['conversation_id'], [u'conversation.id'], ),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('conversation',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###