import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

wine=pd.read_csv('wine.csv')

data=wine[['alcohol','sugar','pH']].to_numpy()
target=wine['class'].to_numpy()

train_input,test_input,train_target,test_target=train_test_split(data,target,stratify=target,test_size=0.2,random_state=42)
print(train_input.shape,test_input.shape)
ss=StandardScaler()
ss.fit(train_input)

train_scaled=ss.transform(train_input)
test_scaled=ss.transform(test_input)

# lr=LogisticRegression()
# lr.fit(train_scaled,train_target)

dt=DecisionTreeClassifier(max_depth=3,random_state=42)
dt.fit(train_scaled,train_target)

plt.figure(figsize=(20,15))
plot_tree(dt,filled=True,feature_names=['alcohol','sugar','pH'])
plt.show()