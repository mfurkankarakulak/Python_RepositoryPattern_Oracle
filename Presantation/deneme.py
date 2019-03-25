# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:33:31 2019

@author: furkan.karakulak
"""

from Infastructer.DataBaseContext.Context import Context
from Entity.Models.DenemeTable import DenemeTable
from Entity.Models.Country import Country


adana = Context()

newValue = DenemeTable( name = "ABdulllah",lastname="Külbstı")
secondValue = Country(countryname="ameriga")

adana.context.products.add(newValue)
adana.context.products.add(secondValue)

adana.context.commit()

