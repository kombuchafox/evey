"""empty message

Revision ID: c23cba6a76d8
Revises: None
Create Date: 2016-06-05 01:22:47.373552

"""

# revision identifiers, used by Alembic.
revision = 'c23cba6a76d8'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messenger_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('messenger_uid', sa.String(length=64), nullable=True),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('profile_pic_id', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_messenger_user_first_name'), 'messenger_user', ['first_name'], unique=False)
    op.create_index(op.f('ix_messenger_user_last_name'), 'messenger_user', ['last_name'], unique=False)
    op.create_index(op.f('ix_messenger_user_messenger_uid'), 'messenger_user', ['messenger_uid'], unique=True)
    op.create_index(op.f('ix_messenger_user_profile_pic_id'), 'messenger_user', ['profile_pic_id'], unique=True)
    op.create_table('fb_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fb_uid', sa.String(length=64), nullable=True),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('profile_pic_id', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fb_user_fb_uid'), 'fb_user', ['fb_uid'], unique=True)
    op.create_index(op.f('ix_fb_user_first_name'), 'fb_user', ['first_name'], unique=False)
    op.create_index(op.f('ix_fb_user_last_name'), 'fb_user', ['last_name'], unique=False)
    op.create_index(op.f('ix_fb_user_profile_pic_id'), 'fb_user', ['profile_pic_id'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('fb_uid', sa.String(length=64), nullable=True),
    sa.Column('messenger_uid', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('did_onboarding', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('date_conv_session', sa.Integer(), nullable=True),
    sa.Column('location_conv_session', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_date_conv_session'), 'user', ['date_conv_session'], unique=False)
    op.create_index(op.f('ix_user_date_created'), 'user', ['date_created'], unique=False)
    op.create_index(op.f('ix_user_did_onboarding'), 'user', ['did_onboarding'], unique=False)
    op.create_index(op.f('ix_user_fb_uid'), 'user', ['fb_uid'], unique=True)
    op.create_index(op.f('ix_user_first_name'), 'user', ['first_name'], unique=False)
    op.create_index(op.f('ix_user_last_name'), 'user', ['last_name'], unique=False)
    op.create_index(op.f('ix_user_location_conv_session'), 'user', ['location_conv_session'], unique=False)
    op.create_index(op.f('ix_user_messenger_uid'), 'user', ['messenger_uid'], unique=True)
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=False)
    op.create_index(op.f('ix_user_password_hash'), 'user', ['password_hash'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('calendar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('conversation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('conversation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['conversation_id'], ['conversation.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_hash', sa.String(), nullable=True),
    sa.Column('calendar_id', sa.Integer(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['calendar_id'], ['calendar.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('event_hash')
    )
    op.create_table('datepoll',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('poll_type', sa.String(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('calendar_event_association',
    sa.Column('calendar_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['calendar_id'], ['calendar.id'], ),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], )
    )
    op.create_table('locationpoll',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('poll_type', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('datepoll_user_association',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('datepoll_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['datepoll_id'], ['datepoll.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('locationpoll_user_association',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('locationpoll_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['locationpoll_id'], ['locationpoll.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('locationpoll_user_association')
    op.drop_table('datepoll_user_association')
    op.drop_table('locationpoll')
    op.drop_table('calendar_event_association')
    op.drop_table('datepoll')
    op.drop_table('event')
    op.drop_table('message')
    op.drop_table('conversation')
    op.drop_table('calendar')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_password_hash'), table_name='user')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_index(op.f('ix_user_messenger_uid'), table_name='user')
    op.drop_index(op.f('ix_user_location_conv_session'), table_name='user')
    op.drop_index(op.f('ix_user_last_name'), table_name='user')
    op.drop_index(op.f('ix_user_first_name'), table_name='user')
    op.drop_index(op.f('ix_user_fb_uid'), table_name='user')
    op.drop_index(op.f('ix_user_did_onboarding'), table_name='user')
    op.drop_index(op.f('ix_user_date_created'), table_name='user')
    op.drop_index(op.f('ix_user_date_conv_session'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_fb_user_profile_pic_id'), table_name='fb_user')
    op.drop_index(op.f('ix_fb_user_last_name'), table_name='fb_user')
    op.drop_index(op.f('ix_fb_user_first_name'), table_name='fb_user')
    op.drop_index(op.f('ix_fb_user_fb_uid'), table_name='fb_user')
    op.drop_table('fb_user')
    op.drop_index(op.f('ix_messenger_user_profile_pic_id'), table_name='messenger_user')
    op.drop_index(op.f('ix_messenger_user_messenger_uid'), table_name='messenger_user')
    op.drop_index(op.f('ix_messenger_user_last_name'), table_name='messenger_user')
    op.drop_index(op.f('ix_messenger_user_first_name'), table_name='messenger_user')
    op.drop_table('messenger_user')
    ### end Alembic commands ###