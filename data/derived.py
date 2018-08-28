import os, json
class Derived:
    def __init__(self):
        """
        hahahah
        """
        self.file = 'data/derived.json'
        if not os.path.exists(self.file):os.system('type NUL >'+self.file)

        f = open(self.file, 'r')
        data = f.read()
        if data=='':data=[]
        else: data = json.loads(data)
        f.close()
        self.data = data

    def add_derived(self, values=None):
        '''
        values=[
            'derived_name',
            'x=col_name',
            'f(x)'
        ]
        '''
        for x in self.data:
            if values[0] in x:
                return 0, 'name exists'
        print('')
        d = {
            'name':values[0],
            'x':values[1],
            'fx':values[2]

        }
        self.data.append(d)
    
    

    def save(self):
        f = open(self.file, 'w')
        f.write(json.dumps(self.data))
        f.close()
    
    def get_all(self):
        return json.dumps(self.data)     