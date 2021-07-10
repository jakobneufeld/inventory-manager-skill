from mycroft import MycroftSkill, intent_file_handler


class InventoryManager(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('manager.inventory.intent')
    def handle_manager_inventory(self, message):
        self.speak_dialog('manager.inventory')


def create_skill():
    return InventoryManager()

