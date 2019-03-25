from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

base  = declarative_base()

class DenemeTable(base):
    
    __tablename__ = 'denemetable'
    
    name = Column(String, primary_key=True)
    lastname = Column(String)
    
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        
    