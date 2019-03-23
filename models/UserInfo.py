# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:01:59 2019

@author: Furkan
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

base  = declarative_base()

class UserInfo(base):
    
    __tablename__ = "userInfo"
    
    id = Column(Integer, primary_key=True)
    userName = Column(String)
    userSurName = Column(String)
    userEmail = Column(String)
    password = Column(String)
    
    
    def __init__(self,userName,userSurName,userEmail,password):
        self.userName = userName
        self.userSurName = userSurName
        self.userEmail = userEmail
        self.password = password
        
    