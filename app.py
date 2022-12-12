#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, request, render_template
import pickle

import numpy

app = Flask(__name__)

model_file = open('modeldami.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', case=0, unit_cost=0)
                           
@app.route('/predict', methods=['POST'])
def predict():
    
    kddati2, tkp, peserta = [x for x in request.form.values()]
    
    data = []
    
    data.append(float(kddati2))
    data.append(float (tkp))
    data.append(float(peserta))
    
    prediction = model.predict([data])
    output = round(float(prediction[0]),2)
    return render_template('index.html', case=output1, unit_cost=output2, kddati2=kddati2, tkp=tkp, peserta=peserta)

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




