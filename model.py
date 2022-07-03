#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
df=pd.read_excel('project1.xlsx')
df
x=df[['DOC', 'Salinity (ppt)', 'TSS (ml/L)',  'Average DO (ppm)', 'TDF (kg)']]
y=df['ABW (gm)']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor(n_estimators=100, min_samples_split=2, min_samples_leaf=2)
rf.fit(x_train, y_train)
pickle.dump(gbrreg, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))

