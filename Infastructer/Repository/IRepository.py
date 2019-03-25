# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:41:49 2019

@author: furkan.karakulak
"""

from abc import ABC, abstractmethod

class Repository(ABC):
    
    """A Repository abstracts the notion of a data store.
        The basic repository pattern has three methods, Add, Get, and Delete
    """
    def __init__(self, uow_man):
        self.uow = uow_man
    
    @abstractmethod
    def add(self, entity):
        """ Insert a new entity into the data store"""
        raise NotImplementedError("add")

    @abstractmethod
    def delete(self, id):
        """Remove a persistent entity from the datastore"""
        raise NotImplementedError("delete")
        
    @abstractmethod
    def get(self, id):
        """Fetch an entity from the datastore by its identifier.
            Changes to the entity will be tracked, and automatically saved
            back to the database when the UnitOfWork is committed"""
        raise NotImplementedError("get")
        
