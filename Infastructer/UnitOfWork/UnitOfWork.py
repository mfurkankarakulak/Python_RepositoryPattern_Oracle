# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:49:01 2019

@author: furkan.karakulak
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Infastructer.UnitOfWork.IUnitOfWork import UnitOfWorkManager,UnitOfWork
from Infastructer.Repository.Repository import SqlAlchemyRepository

class SqlAlchemyUnitOfWorkManager(UnitOfWorkManager):

    engine = create_engine("postgresql://postgres:123@localhost:5432/mypythondb")
    Session = sessionmaker(engine)  
    session = Session()
    
    def start(self):
        return SqlAlchemyUnitOfWork(self.session)


class SqlAlchemyUnitOfWork(UnitOfWork):

    def __init__(self, session):
        self.session = session
        self.committed = False
        self._products = SqlAlchemyRepository(session)
        
    
    def __enter__(self):
        self.session.begin()

    def __exit__(self, value, type, traceback):
        if(self.committed is False):
            self.session.rollback()
        self.session.close()

    def rollback(self):
        self.session.rollback()
        self.session.close()
        self.committed = True

    def commit(self):
        self.session.flush()
        self.session.commit()
        self.session.close()
        self.session.committed = True

    @property
    def products(self):
        return self._products