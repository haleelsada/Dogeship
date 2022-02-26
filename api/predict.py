import joblib
import numpy as np
import pandas as pd


def predict_close():
    model = joblib.load('linear_model')
    columns = ['Open', 'High', 'Low', 'Close', 'Volume', '7day_open', '7day_close',
               '7day_high', '7day_low', '40day_open', '40day_close', '40day_high', '40day_low']
    arr = [0.000221, 0.000229, 0.000214, 0.000216, 281158, 0.00025,
           0.000216, 0.000258, 0.000214, 0.000347, 0.000216, 0.000467, 0.000214]
    dic = {columns[i]: [arr[i]] for i in range(len(arr))}
    arr = pd.DataFrame(dic)
    return model.predict(arr)


if __name__ == '__main__':
    result = predict_close()
    print(result[0])
