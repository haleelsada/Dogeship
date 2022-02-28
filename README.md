<<<<<<< HEAD
# Dogeship API

![](https://i.pinimg.com/736x/11/3e/47/113e4759bce931c842b6b96960b6f4d2.jpg)
=======
# Dogeship
>>>>>>> 8df0e02a8b8041d6d08ef0bea87d58b987f5cc01

#### Built as a part of Tinkerhub Co-Coder 2022 Event.

### **[Website](https://haleelsada.github.io/Dogeship/)**
### **[Webapp/API](https://dogecoin-prediction-bot.herokuapp.com/)**
### **[ML Model Notebook](https://github.com/haleelsada/Dogeship/blob/main/model/model_training.ipynb)**

## A project to predict the price of Doge cryptocurrency of any date based on previous data. 

### How it Works ?
A Machine Learning model with an architecture including Linear regression and the model was trained on it.

The project website can be found **[here](https://haleelsada.github.io/Dogeship/)**. Doge price gets produced when the user inputs the parameters and clicks the `Predict` button. The website was built using HTML, CSS and JS along with an API request and response which deployed in heroku. On pressing the `Predict` button, an API GET request gets called which returns the price. The source code regarding the api and website can be found in the **[api](https://github.com/haleelsada/Dogeship/tree/main/api)** and **[frontend](https://github.com/haleelsada/Dogeship/tree/main/frontend)** folders respectively.

The dataset collected was splitted into train and validation in the ratio 80:20.  Minimal Data Preprocessing was done on the collected dataset, more parameters are generated from the existing dataset. Training was carried out in Goole Colab and the jupyter notebook used for training and validation can be found **[here](https://github.com/haleelsada/Dogeship/blob/main/model/model_training.ipynb)**.

### Libraries used
      
  - pandas 

  - numpy 

  - joblib

  - matplotlib

  - scikit-learn

  - flask

### How to use

Inorder to train the model, load the python jupyter notebook found **[here](https://github.com/haleelsada/Dogeship/blob/main/model/model_training.ipynb)** in a Google Colab and make a copy of it for your use.<br>
To predict the price use the Website found **[here](https://haleelsada.github.io/Dogeship/)**.

## API

API is built using Flask framework and hosted in Heroku.

- Plant Disease Detection

    Accepts a POST request with input features as a dictionary and returns a dictionary with close price prediction.
    

#### How to use

API has been built on this Regression Model. URL = "https://dogecoin-prediction-bot.herokuapp.com/"

User has to send a POST request to the given api with a dictionary of Input Features. 

```python
import requests

columns = ['Open', 'High', 'Low', 'Close', 'Volume', '7day_open', '7day_close',
               '7day_high', '7day_low', '40day_open', '40day_close', '40day_high', '40day_low']
# Sample Inputs
arr = [0.000293, 0.000299, 0.00026, 0.000268, 1463600, 0.000287714285714,
           0.000290571428571, 0.000325, 0.00026, 0.000300025, 0.000298775, 0.000467, 0.000223]
dic = {columns[i]: arr[i] for i in range(len(arr))}

url="https://dogecoin-prediction-bot.herokuapp.com/"
r = requests.post(url,json = dic)
print(r.text)
```
Output
```python
'{"close":0.0003021457613296437}\n'
```

## Contributors

<table>
  <tr>

 <td align="center"><a href="https://github.com/haleelsada"><img src="https://avatars.githubusercontent.com/u/75977159?v=4" width="180px;" alt=""/><br /><sub><b>Haleel sada</b></sub></a><br />        

<td align="center"><a href="https://github.com/nandakishormpai"><img src="https://avatars.githubusercontent.com/u/57388834?v=4" width="180px;" alt=""/><br /><sub><b>Nanda Kishor M Pai</b></sub></a><br />


</tr>
</table>
