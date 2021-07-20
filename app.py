#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020
@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from sal import money
import numpy as np
import pickle
import pandas as pd
from fastapi.responses import FileResponse
from fastapi import FastAPI,UploadFile,File
# 2. Create the app object
app = FastAPI()
pickle_in = open("lr.pkl","rb")
lr=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_salary(data:money):
    data = data.dict()
    jobType_CEO=data['jobType_CEO']
    jobType_CFO=data['jobType_CFO']
    jobType_CTO=data['jobType_CTO']
    jobType_JANITOR=data['jobType_JANITOR']
    jobType_JUNIOR=data['jobType_JUNIOR']
    jobType_MANAGER=data['jobType_MANAGER']
    jobType_SENIOR=data['jobType_SENIOR']
    jobType_VICE_PRESIDENT=data['jobType_VICE_PRESIDENT']
    yearsExperience=data['yearsExperience']
    milesFromMetropolis=data['milesFromMetropolis']
    
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = lr.predict([[jobType_CEO,jobType_CFO,jobType_CTO,jobType_JANITOR,jobType_JUNIOR,jobType_MANAGER,jobType_SENIOR,jobType_VICE_PRESIDENT, yearsExperience,milesFromMetropolis]])
    return {
        'prediction':prediction[0][0]
    }



       

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload

