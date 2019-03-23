# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:15:02 2019

@author: Furkan
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

base = declarative_base()

class City(base):
    
    __tablename__ = "City"
    
    id = Column(Integer, primary_key=True)
    cityName = Column(String)
    countryId = Column(Integer)
    
    def __init__(self,cityName,countryId):
        self.cityName = cityName
        self.countryId = countryId
  
    