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
