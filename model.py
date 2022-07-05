#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pickle
df=pd.read_excel('project1.xlsx')
df
x=df[['DOC', 'Salinity (ppt)', 'TSS (ml/L)',  'Average DO (ppm)', 'TDF (kg)']]
y=df['ABW (gm)']
from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor(n_estimators=100, min_samples_split=2, min_samples_leaf=2)
rf.fit(x, y)
pickle.dump(rf, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))


# In[ ]:




