from mycroft import MycroftSkill, intent_file_handler


class Timemannage(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('timemannage.intent')
    def handle_timemannage(self, message):
        self.speak_dialog('timemannage')


def create_skill():
    return Timemannage()

