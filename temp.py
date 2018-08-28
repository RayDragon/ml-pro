# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 03:50:07 2018

@author: Govind Singh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
data = pd.read_csv('data/actual.csv')

from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

data['time']=data.iloc[:, -1].values%(60*60*24)
y=data.iloc[:, [6]].values
x=data.iloc[:, [-1]]

cl = DecisionTreeClassifier()

tr = StandardScaler()
x=tr.fit_transform(x)

cl.fit(x,y)
xx = np.arange(0, 60*60*24).reshape((-1,1))
xxx = tr.transform(xx)
pt.plot(xx, cl.predict(xxx))
#cl.predict()