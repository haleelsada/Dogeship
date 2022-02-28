# Dogeship

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

Inorder to train the model, load the python jupyter notebook found **[here](https://github.com/haleelsada/Dogeship/blob/main/model/model_training.ipynb)** in a Google Colab and make a copy of it for your use. To predict the price use the Website found **[here](https://haleelsada.github.io/Dogeship/)**.
