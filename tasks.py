import json
class Task:
    TYPE_StoC, TYPE_CtoS=0,1
    def __init__(self, name, values, Type=TYPE_CtoS):
        """
        this is gonna be fun
        """
        self.type = Type
        self.name = name
        self.values = values
    
    def get_json(self):
        return None
