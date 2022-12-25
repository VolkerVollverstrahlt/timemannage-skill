from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
from database import Database


class Timemannage(MycroftSkill):
    
    
    
    def __init__(self):
        MycroftSkill.__init__(self)
        self.db = Database()


    @intent_handler(IntentBuilder("read")
                    .require('what')
                    .require('todos')
                    .optinally('todo_name')
                    .optinally('todo_attribute'))
    def handle_timemannage(self, message):
        data = {'todo_name' : message.data.get('todo_name'), 'todo_attribute' : message.data.get('todo_attribute')}
        
        if data['todo_name']:
            if not self.db.Todo_exists(data("todo_name")):
                self.speak_dialog('todo.not.found',data)
                
            elif self.db.Todo_empty( "todo_name"):
                self.speak_dialog('todo.no.attributes',data)
                
            else:
                if data['todo_attribute']:
                    
                    pass
            

def create_skill():
    return Timemannage()

