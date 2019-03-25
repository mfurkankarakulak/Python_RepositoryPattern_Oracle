# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:27:20 2019

@author: furkan.karakulak
"""

from Infastructer.UnitOfWork.UnitOfWork import SqlAlchemyUnitOfWorkManager,SqlAlchemyUnitOfWork
from Entity.Models.City import City
from Entity.Models.UserInfo import UserInfo
from Entity.Models.Country import Country
from Entity.Models.DenemeTable import DenemeTable


class Context:
    
    def __init__(self):
        self.context = SqlAlchemyUnitOfWorkManager().start()
        
    def UserInfo():
        return UserInfo()
    
    def City():
        return City()
    
    def Country():
        return Country()
    
    def DenemeTable():
        return DenemeTable()
      
    
        


        
       



