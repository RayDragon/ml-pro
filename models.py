from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
#import matplotlib.pyplot as pt

class Models:
    def __init__(self, table=pd.DataFrame(), cols=[]):
        y=cols[0]
        x=cols[1:]
        
        self.x=x
        print(x,y)
        self.table=table
        self.transformer = StandardScaler()
        self.Y = table.loc[:, y].values
        self.X = self.transformer.fit_transform(table.loc[:, x].values, y=self.Y)
        #pt.plot(self.X, self.Y)
        #pt.show()
        self.train()
    
    def train(self):
        cl = DecisionTreeClassifier()
        cl.fit(self.X, self.Y)
        self.model = cl
        #pt.plot(self.X, self.model.predict(self.X))
        #pt.show()
    
    def predict(self, val):
        val = self.transformer.transform(val)
        return self.model.predict(val)
        

    