# -*- coding:utf-8 -*-

from app_tt.core import db
from app_tt.engine.models import *

def record_book_info_mbdb(info_book):
    bk = book.query.filter_by(id=info_book['bookid']).first()

    if (bk != None):
        print("The book " + bk.title + " already exists in mbdb.")
        return
    
    bk = book(info_book['bookid'],
              info_book['title'],
              info_book['publisher'],
              info_book['contributor'],
              info_book['volume'],
              info_book['img'])   
    try:
        db.session.add(bk)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    
    
def record_page(page_info):
    pg = page(page_info[0],
              page_info[1])
    
    try:
        db.session.add(pg)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e