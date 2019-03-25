# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:01:59 2019

@author: Furkan
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

base  = declarative_base()

class UserInfo(base):
    
    __tablename__ = "userinfo"
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    userlastname = Column(String)
    useremail = Column(String)
    password = Column(String)
    
    
    def __init__(self,username,userlastname,useremail,password):
        self.username = username
        self.userlastname = userlastname
        self.useremail = useremail
        self.password = password
        
    