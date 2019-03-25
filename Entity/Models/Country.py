# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:19:23 2019

@author: Furkan
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

base = declarative_base()

class Country(base):
    
    __tablename__ = 'country'
    
    id = Column(Integer, primary_key=True)
    countryname = Column(String)
    
    def __init__(self,countryname):
        self.countryname = countryname
        
  
    