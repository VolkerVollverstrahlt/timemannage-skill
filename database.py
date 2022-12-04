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
        self.JSON_PATH =join(dirname(__file__), 'data.json')
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
            json.dump(self.jason_data, json_file)
            
            
    # checks
    def Todo_item_exists(self, todo, item):
        return item in self.jason_data[todo]
    
    def no_Todos(self):
        return True if len(list(self.jason_data.keys())) == 0 else False
    
    def Todo_empty(self, todo):
        return not bool(self.jason_data[todo])
    
    def Todo_exists(self, todo):
        return True if todo in self.jason_data.keys() else False
    
    # reads
    def read_item(self, todo, item):
        return self.jason_data[todo][item]
    
    def read_todo(self, todo):
        return self.jason_data[todo]
    
    def read_todos(self):
        return list(self.jason_data.keys())
    
    # adds
    def add_todo(self, todo):
        self.jason_data[todo] = {}
        self.write_data()
        
    def add_todo_charas(self, todo, char, wert):
        self.jason_data[todo][char] = wert
        self.write_data()
        
    def add_list_char(self, todo, char,point):
        if Database.Todo_item_exists(self,todo, char) and self.jason_data[todo][char] != None:
            self.jason_data[todo][char].append(point)
            self.write_data()
        else:
            self.jason_data[todo][char] = []
            self.jason_data[todo][char].append(point)
            self.write_data()
            
    # del
    def del_Todo(self, Todo):
        del self.jason_data[Todo]
        self.write_data()
        
    def del_char(self, Todo, char):
        del self.jason_data[Todo][char]
        self.write_data()
    
    

    