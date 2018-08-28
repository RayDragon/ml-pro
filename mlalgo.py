import pandas as pd
import os
from data.sources import Source
from data.derived import Derived
from data.outcome import Outcome
from models import Models

class Runner:
    def __init__(self):
        self.file_actual = 'data/actual.csv'
        self.file_predicted = 'data/predicted.csv'
        sr = Source()
        cols = []
        # column_names from sources
        for data in sr.data:
            name = [d for d in data][0]
            col = data[name]
            for c in col:
                c = name+"_"+c
                cols.append(c)
        # now column names from derived
        dr = Derived()
        for data in dr.data:
            cols.append(data['name'])
        
        # now the outcome which provides the col names which will be required for prediction/training
        self.out = Outcome()

        df = pd.DataFrame(columns=cols)
        if not os.path.exists(self.file_actual):df.to_csv(self.file_actual, index=False)
        if not os.path.exists(self.file_predicted):df.to_csv(self.file_predicted, index=False)

        self.datas = {
            'actual':pd.read_csv(self.file_actual),
            'predicted':pd.read_csv(self.file_predicted)
        }

    
    def add_data_from_csv(self, file_name='data/temp.csv'):
        # convert data

        ndata=pd.read_csv('data/temp.csv')
        sr = Source()
        for data in sr.data:
            name = [d for d in data][0]
            col = data[name]
            if all(x in col for x in ndata):
                # yep we got the nam
                new_col=[]
                for n in ndata.columns:
                    new_col.append(name+"_"+n)
                ndata.columns=new_col
        self.datas['actual']=self.datas['actual'].append(ndata, sort=True)
    
    def get_models(self):
        self.md = []
        out = Outcome()
        for x in out.data:
            name = [c for c in x][0]
            #print(name)
            model = Models(self.datas['actual'], x[name])
            self.md.append({
                'name':name,
                'model':model
            })



        #m=Models()

    def find_derived(self):
        der = Derived()
        for d in der.data:
            x = self.datas['actual'][d['x']]
            #print(x.head())
            self.datas['actual'][d['name']]=eval(d['fx'])
            #print(self.datas['actual'])

    def save(self):
        self.datas['actual'].to_csv(self.file_actual, index=False)
        self.datas['predicted'].to_csv(self.file_predicted, index=False)

    # data can be added/saved
    # now we need to find what we need to train and values we need to predict

'''
rn = Runner()
rn.find_derived()
rn.get_models()
# rn.add_data_from_csv()
# rn.save()
import numpy as np
import matplotlib.pyplot as pt
md=rn.md[0]['model']
x=md.transformer.inverse_transform(md.X)
pt.plot(x, md.predict(x))
y=md.predict(x)

xx=np.arange(0, 24*60*60).reshape(-1,1)
pt.plot(xx, md.predict(xx))
md.predict(60000)
'''



