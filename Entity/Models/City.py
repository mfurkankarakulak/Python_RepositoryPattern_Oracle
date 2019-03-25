# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:15:02 2019

@author: Furkan
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

base = declarative_base()

class City(base):
    
    __tablename__ = "city"
    
    id = Column(Integer, primary_key=True)
    cityname = Column(String)
    countryid = Column(Integer)
    
    def __init__(self,cityname,countryid):
        self.cityname = cityname
        self.countryid = countryid

