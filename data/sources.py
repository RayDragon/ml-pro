import json

class Source:
    def __init__(self):
        ''
        self.file = 'data/sources.json'
        f = open(file, 'r')
        data = json.loads(f.read())
        f.close()
        self.data = data

    def add_source(self, values=None):
        '''
        values=[
            'source_name',
            'comma seperated col_names'
        ]
        '''
        for x in self.data:
            if values[0] in x:
                return 0, 'name exists'
        
        d = {
            values[0]:values[1].split(',')
        }
        self.data.append(d)
    
    def save(self):
        f = open(self.file, 'w')
        f.write(json.dumps(self.data))
        f.close()
    
    def get_all(self):
        return json.dumps(self.data)

        
        

