#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, request, render_template
import pickle

import numpy

app = Flask(__name__)

model_file1 = open('modeldamicost.pkl', 'rb')
model1 = pickle.load(model_file1, encoding='bytes')

model_file2 = open('modeldamicase.pkl', 'rb')
model2 = pickle.load(model_file2, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', unit_cost=0, case=0)
                           
@app.route('/predict', methods=['POST'])
def predict():
    
    kddati2, tkp, peserta, tglpelayanan = [x for x in request.form.values()]
    
    data = []
    
    data.append(float(kddati2))
    data.append(float(tkp))
    data.append(float(peserta))
    data.append(float(tglpelayanan))
    
    try:
        prediction = model1.predict([data])
        output1 = round(float(prediction[0]),2)
    except:
        output1=0
    try:
        prediction = model2.predict([data])
        output2 = round(float(prediction[0]),2)
    except:
        output2=0
    
    return render_template('index.html', unit_cost=output1, case=output2, kddati2=kddati2, tkp=tkp, peserta=peserta, tglpelayanan=tglpelayanan)

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




