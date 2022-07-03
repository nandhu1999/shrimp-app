# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 22:27:05 2022

@author: user
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    feature_list = request.form.to_dict()
    feature_list = list(feature_list.values())
    feature_list = list(map(int, feature_list))
    final_features = np.array(feature_list).reshape(1, 12) 
    
    prediction = model.predict(final_features)
    return render_template('index.html', prediction_text='Average shrimp body weight is {}'.format(text))


if __name__ == "__main__":
    app.run(debug=True)
