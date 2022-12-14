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
                    .optinally('todo_name'))
    def handle_timemannage(self, message):
        self.speak_dialog('timemannage')


def create_skill():
    return Timemannage()

