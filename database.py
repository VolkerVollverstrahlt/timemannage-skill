# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:21:07 2022

@author: Yannik

zugrundelegiegende struktur von https://github.com/lb803/list-manager-skill/blob/master/database.py mit 
anpassungen für meine Datanspeicherstruktur
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
            
            
    # checks
    def Todo_item_exists(self, todo, item):
        return item in self.jason_data[todo]
    
    def no_Todos(self):
        return True if len(list(self.jason_data.keys())) == 0 else False
    
    def Todo_empty(self, todo):
        return not bool(self.jason_data[todo])
    
    def Todo_exists(self, todo):
        return True if todo in self.jason_data.keys() else False
    
    #
            
    