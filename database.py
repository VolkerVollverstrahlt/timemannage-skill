# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:21:07 2022

@author: Yannik
"""

import json
from os.path import dirname, join

class Database:
    
    
    
    
    
    
    def __init__(self):
        self.JSON_PATH =join(dirname(__file__), 'data.jasn')
        try:
            self.jason_data = self.read_data()
        except FileNotFoundError:
            self.jason_data = {}
            self.write_data()
    
    
    #file loading and saving
    def read_data(self):
        with open(self.JSON_PATH, 'r') as json_file:
            return json.load(json_file)
        
    def write_data(self):
        with open(self.JSON_PATH, 'w') as json_file:
            json.dump(self.json_data, json_file)
            
    