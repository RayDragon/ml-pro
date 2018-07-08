import json

class Settings:
    def __init__(self, folder_name='settings', load_saved=True):
        self.folder = folder_name
        if load_saved==True:
            files = open(folder_name+'/settings.json','r')
            data = files.read()
            self.settings = json.loads(data)
        else:
            self.settings={}
    
    def save(self):
        data = json.dumps(self.settings)
        file = open(self.folder+"/settings.json", 'w')
        file.write(data)
        file.close()

