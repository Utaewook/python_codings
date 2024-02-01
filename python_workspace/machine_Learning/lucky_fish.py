from numpy.core.fromnumeric import mean
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

fish=pd.read_csv('fish_data.csv')
fish_input=fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()
fish_target=fish['Species'].to_numpy()

train_input,test_input,train_target,test_target=train_test_split(fish_input,fish_target,stratify=fish_target,random_state=42)

mean=np.mean(train_input,axis=0)
std=np.std(train_input,axis=0)
 
kn=KNeighborsClassifier(n_neighbors=3)
kn.fit(train_input,train_target)
print(kn.score(test_input,test_target))