import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes

np.random.seed(2023)

diabetes = load_diabetes()

data, target = diabetes['data'], diabetes['target']

df = pd.DataFrame(data, columns=diabetes['feature_names'])
print(df.describe())

from sklearn.model_selection import train_test_split

train_data, test_data, train_target, test_target = train_test_split(data,target,test_size=0.3)

print(len(data),len(train_data),len(test_data))

print("train ratio : {:.2f}".format(len(train_data)/len(data)))
print("test ratio : {:.2f}".format(len(test_data)/len(data)))

from sklearn.linear_model import LinearRegression
multi_regression = LinearRegression()
multi_regression.fit(train_data, train_target)

print(multi_regression.intercept_, multi_regression.coef_)

pred_train = multi_regression.predict(train_data)
pred_test = multi_regression.predict(test_data)
