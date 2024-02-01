import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 
     1000.0, 1000.0]
     )

df=pd.read_csv('perch.csv')
perch_full=df.to_numpy()

train_input,test_input,train_target,test_target=train_test_split(perch_full,perch_weight,random_state=42)

poly=PolynomialFeatures(degree=5,include_bias=False)
poly.fit(train_input)
train_poly=poly.transform(train_input)
test_poly=poly.transform(test_input)

mean=np.mean(train_input,axis=0)
std=np.std(train_input,axis=0)
train_scaled=(train_input-mean)/std

ss=StandardScaler()
ss.fit(train_poly)

train_scaled=ss.transform(train_poly)
test_scaled=ss.transform(test_poly)

##Ridge 회귀
# ridge=Ridge()
# ridge.fit(train_scaled,train_target)
# print(ridge.score(train_scaled,train_target))

# alpha_list=[0.001,0.01,0.1,1,10,100]
# train_score=[]
# test_score=[]

# for alpha in alpha_list:
#     ridge=Ridge(alpha=alpha)
#     ridge.fit(train_scaled,train_target)
#     train_score.append(ridge.score(train_scaled,train_target))
#     test_score.append(ridge.score(test_scaled,test_target))
    
    
# plt.plot(np.log10(alpha_list),train_score)
# plt.plot(np.log10(alpha_list),test_score)
# plt.xlabel('alpha')
# plt.ylabel('R^2')
# plt.show()

##Lasso 회귀

train_score=[]
test_score=[]

lasso=Lasso()
lasso.fit(train_scaled,train_target)
print(lasso.score(train_scaled,train_target))

print(lasso.score(test_scaled,test_target))

alpha_list=[0.001,0.01,0.1,1,10,100]

for alpha in alpha_list:
    lasso=Lasso(alpha=alpha,max_iter=10000)
    lasso.fit(train_scaled,train_target)
    train_score.append(lasso.score(train_scaled,train_target))
    test_score.append(lasso.score(test_scaled,test_target))

plt.plot(np.log10(alpha_list),train_score)
plt.plot(np.log10(alpha_list),test_score)
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.show()