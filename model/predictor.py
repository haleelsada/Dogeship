# import libraries and trained model 

import joblib
import pandas as pd


#function to predict price
def predicter(arr):
  model=joblib.load('linear_model')
  return model.predict(arr)

#input data from user
def inputer():
  data=[]
  columns=['Open','High','Low','Close','Volume','7day_open','7day_close','7day_high','7day_low','40day_open','40day_close','40day_high','40day_low']
  for i in columns:
    data.append(float(input(i+' :')))
  dic={columns[i]:[data[i]] for i in range(len(columns))}
  arr=pd.DataFrame(dic)
  
  return arr[0:]

# predict
print(predicter(inputer()))







#if extracting weights from model
'''def predicter():
  pred=float(1.2667569472308779e-05)
  weight=[9.06974620e-02,5.46490304e-02,-4.65869174e-01,4.27418746e-01,-1.49158463e-13,-7.97503380e-03,8.31582970e-01,-1.10608523e-01,5.83665697e-02,2.63070450e-03,1.07272439e-01,2.76821456e-03,2.96067291e-03]
  columns=['Open','High','Low','Close','Volume','7day_open','7day_close','7day_high','7day_low','40day_open','40day_close','40day_high','40day_low']
  for i in range(13):
    pred+=(float(input(columns[i]+' :'))*weight[i])
  return pred



print(predicter())'''
