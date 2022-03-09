# Dogeship

A project to predict the price of Doge cryptocurrency of any date based on previous data.

A Machine Learning model with an architecture including Linear regression and the model was trained on it.

The project website can be found **[here](https://haleelsada.github.io/Dogeship/)**. Doge price gets produced when the user inputs the parameters and clicks the `Predict` button. The website was built using HTML, CSS and JS along with an API request and response which deployed in heroku. On pressing the `Predict` button, an API GET request gets called which returns the price. The source code regarding the api and website can be found in the **[api](https://github.com/haleelsada/Dogeship/tree/main/api)** and **[frontend](https://github.com/haleelsada/Dogeship/tree/main/frontend)** folders respectively.

## Team members
1. **[Haleel sada](https://github.com/haleelsada/)**
2. **[Nanda Kishor M Pai](https://github.com/nandakishormpai/)**

## Team Id
**ML / 2**

## Link to product walkthrough
<a href="https://drive.google.com/file/d/1jv2TpHd9e7E1m1rPKhQqkTQizM1AK77w/view?usp=sharing"   title="Product Walkthrough" target="_blank" ><img src="https://github.com/nandakishormpai2001/manglish_lyrics_generator/blob/frontend/images/walk.jpg" alt="Product Walkthrough" /></a>

## How it Works ?
1. Go to **[website](https://haleelsada.github.io/Dogeship/)** and give date and other parameters to predict the Doge price of next day
2. On pressing the `Predict` button, an **[API](https://github.com/haleelsada/Dogeship/tree/main/api)** GET request gets called which returns the price
3. the api uses Linear regression algorithm on previous data to predict the price of Dogecoin
4. The website was built using HTML, CSS and JS along with an API request and response which deployed in heroku

## Libraries used

pandas - 1.3.5

numpy - 1.22.3

joblib - 1.1.0

matplotlib - 3.2.2

scikit-learn - 1.0.2

flask - 1.1.4

## How to configure

Inorder to train the model, load the python jupyter notebook found **[here](https://github.com/haleelsada/Dogeship/blob/main/model/model_training.ipynb)** in a Google Colab and make a copy of it for use. To predict the price use this **[website](https://haleelsada.github.io/Dogeship/)**.

The source code regarding the api and website can be found in the **[api](https://github.com/haleelsada/Dogeship/tree/main/api)** and **[frontend](https://github.com/haleelsada/Dogeship/tree/main/frontend)** directories respectively.

API has been built on this Regression Model. URL could be found here **[here](https://dogecoin-prediction-bot.herokuapp.com/)**

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


## How to Run
The project website could be run from **[here](https://haleelsada.github.io/Dogeship/)**

