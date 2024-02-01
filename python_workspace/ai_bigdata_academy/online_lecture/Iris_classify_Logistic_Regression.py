import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functions import *


np.random.seed(2021)

# Data load
print_title("Data Load")
from sklearn.datasets import load_iris

iris = load_iris()
print(iris["feature_names"])
print(iris["target_names"])

data, target = iris['data'], iris['target']

# data eda
print_title("Data EDA")
print(pd.DataFrame(data, columns=iris["feature_names"]).describe())
print(pd.Series(target).value_counts())

# data split
print_title("Data Split")
from sklearn.model_selection import train_test_split

train_data,test_data, train_target, test_target = train_test_split(data,target,train_size=0.7,random_state=2023,stratify=target)
