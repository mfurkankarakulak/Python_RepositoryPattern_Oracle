# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:44:20 2019

@author: furkan.karakulak
"""

from Infastructer.Repository.IRepository import Repository

class SqlAlchemyRepository(Repository):

    def __init__(self, session):
        self._session = session
        
    def add(self, entity):
        self._session.add(entity)
        
    def delete(self, entity):
        self._session.delete(entity)

    def get(self, id):
        self._session.query().get(id)