import json

class Outcome:
    def __init__(self):
        ''
        self.file = 'data/outcome.json'
        f = open(self.file, 'r')
        data = f.read()
        if data=='': data=[]
        else: data = json.loads(data)
        f.close()
        self.data = data

    def add_outcome(self, values=None):
        '''
        values=[
            'outcome_name',
            'comma seperated col_names'
        ]
        '''
        for x in self.data:
            if values[0] in x:
                return 0, 'name exists'
        
        d = {
            values[0]:[x.strip() for x in values[1].split(',')]
        }
        self.data.append(d)
    
    def save(self):
        f = open(self.file, 'w')
        f.write(json.dumps(self.data))
        f.close()
    
    def get_all(self):
        return json.dumps(self.data)

        
        

