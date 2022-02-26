import joblib
import numpy as np
import pandas as pd


def predict_close(arr):
    model = joblib.load('model_files/linear_model')
    columns = ['Open', 'High', 'Low', 'Close', 'Volume', '7day_open', '7day_close',
               '7day_high', '7day_low', '40day_open', '40day_close', '40day_high', '40day_low']

    dic = {columns[i]: [arr[i]] for i in range(len(arr))}
    arr = pd.DataFrame(dic)
    return model.predict(arr)


if __name__ == '__main__':
    arr = [0.000293, 0.000299, 0.00026, 0.000268, 1463600, 0.000287714285714,
           0.000290571428571, 0.000325, 0.00026, 0.000300025, 0.000298775, 0.000467, 0.000223]
    result = predict_close(arr)
    print(result[0])
