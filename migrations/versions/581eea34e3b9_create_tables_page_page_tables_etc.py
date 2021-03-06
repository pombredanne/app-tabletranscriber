"""
    create tables fact, page_table, metadata, cell, report and workflow_transaction
    and add constraints 'on update cascade and on delete cascade to book_id in page
    table.


Revision ID: 581eea34e3b9
Revises: 3bb24cc527a8
Create Date: 2014-03-11 11:55:36.604900

"""

# revision identifiers, used by Alembic.
revision = '581eea34e3b9'
down_revision = '3bb24cc527a8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_constraint('page_book_id_fkey', 'page')
    
    op.create_foreign_key('page_book_id_fkey', 'page', 'book',
                          ['book_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    
    op.create_table('fact',
        sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('user_id', sa.String(255)),
        sa.Column('book_id', sa.String(255)),
        sa.Column('page_id', sa.Integer, nullable=False), 
        sa.Column('top_pos', sa.Integer, nullable=False),
        sa.Column('left_pos', sa.Integer, nullable=False),
        sa.Column('bottom_pos', sa.Integer, nullable=False),
        sa.Column('right_pos', sa.Integer, nullable=False),
        sa.Column('post_id', sa.String(255)),
        sa.Column('fact_text', sa.String(255))
    )
    
    op.create_table('page_table',
        sa.Column('id', sa.Integer, autoincrement=True),
        sa.Column('page_id', sa.Integer),
        sa.Column('book_id', sa.String(100)),
        sa.Column('initialDate', sa.Date),
        sa.Column('finalDate', sa.Date),
        sa.Column('local_url', sa.String(255)),
        sa.Column('top_pos', sa.Integer, sa.CheckConstraint('top_pos >= 0')),
        sa.Column('left_pos', sa.Integer, sa.CheckConstraint('left_pos >= 0')),
        sa.Column('right_pos', sa.Integer, sa.CheckConstraint('right_pos >= 0')),
        sa.Column('bottom_pos', sa.Integer, sa.CheckConstraint('bottom_pos >= 0')),
        
        sa.PrimaryKeyConstraint('id', 'page_id', 'book_id'),
        sa.ForeignKeyConstraint(['page_id', 'book_id'], ['page.id', 'page.book_id'], 
                                onupdate='CASCADE', ondelete='CASCADE')
    )
    
    op.create_table('metadata',
        sa.Column('id', sa.Integer, autoincrement=True),
        sa.Column('page_table_id', sa.Integer), 
        sa.Column('page_id', sa.Integer),
        sa.Column('book_id', sa.String(100)),
        sa.Column('source', sa.String(255)),
        sa.Column('footer', sa.String(255)),
        sa.Column('title', sa.String(255)),
        sa.Column('subtitle', sa.String(255)),
        sa.Column('subject', sa.String(255)),
        
        sa.PrimaryKeyConstraint('id', 'page_table_id', 'page_id', 'book_id'),
        sa.ForeignKeyConstraint(['book_id', 'page_id', 'page_table_id'],
                                ['page_table.book_id', 'page_table.page_id', 'page_table.id'],
                                 onupdate='CASCADE', ondelete='CASCADE')
    )
    
    op.create_table('cell',
        sa.Column('id', sa.Integer, autoincrement=True),            
        sa.Column('x0', sa.Integer, sa.CheckConstraint('x0 >= 0')),
        sa.Column('y0', sa.Integer, sa.CheckConstraint('y0 >= 0')),
        sa.Column('x1', sa.Integer, sa.CheckConstraint('x1 >= 0')),
        sa.Column('y1', sa.Integer, sa.CheckConstraint('y1 >= 0')),
        
        sa.Column('text', sa.String(255)),
        
        sa.Column('page_table_id', sa.Integer), 
        sa.Column('page_id', sa.Integer),
        sa.Column('book_id', sa.String(100)),
        
        sa.PrimaryKeyConstraint('id', 'page_table_id', 'page_id', 'book_id'),
        
        sa.ForeignKeyConstraint(['page_table_id', 'page_id', 'book_id'], 
                                ['page_table.id', 'page_table.page_id', 'page_table.book_id'],
                                 onupdate='CASCADE', ondelete='CASCADE')
    ) 

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
        sa.Column('id', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
        sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
        sa.Column('publisher', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
        sa.Column('contributor', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
        sa.Column('volume', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
        sa.Column('img_url', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name=u'book_pkey')
    )
    
    op.create_table('page',
        sa.Column('id', sa.INTEGER(), server_default="nextval('page_id_seq'::regclass)", nullable=False),
        sa.Column('book_id', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
        sa.Column('archiveURL', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column('page', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(['book_id'], [u'book.id'], name=u'page_book_id_fkey'),
        sa.PrimaryKeyConstraint('id', 'book_id', name=u'page_pkey')
    )
    ### end Alembic commands ###
