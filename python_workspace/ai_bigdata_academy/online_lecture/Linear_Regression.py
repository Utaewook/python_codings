import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(2023)

# 1 Univariate Regression

x = np.array([1,2,3,4])
y = np.array([2,1,4,3])

# plt.scatter(x,y)
# plt.show()

# scikit-learn 모듈에서 모델 학습을 하려면 데이터는 (n,c)형태로 되어있어야함
# n = 데이터의 개수  /  c = feature의 개수
# 위에서 생성한 데이터는 4개의 데이터와 1개의 feature로 이루어져 있음

print(x,x.shape)
data = x.reshape(-1,1)
print(data,data.shape)


from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X=data,y=y)

print(model.intercept_,model.coef_)  # bias와 coef(편향) 값 확인

pred = model.predict(data)
print(pred)
pred2 = model.predict([[7]])
print(pred2)
# plt.scatter(x,y)
# plt.plot(x,pred,color='green')
# plt.show()



# 2 Multivariate Regression
bias = 1
beta = np.array([2,3,4,5]).reshape(4,1)
noise = np.random.randn(100,1)

x = np.random.randn(100,4)
y = bias + x.dot(beta)
y_with_noise = y+noise

model = LinearRegression()
model.fit(x,y_with_noise)

print(model.intercept_,model.coef_) # bias와 편향 값 확인
pred = model.predict(x)
print(pred)

# 통계적 방법을 통한 확인
bias_x = np.array([1]*len(x)).reshape(-1,1)
stat_x = np.hstack([bias_x,x])
x_x_transposed = stat_x.transpose().dot(stat_x)
x_x_transposed_inverse = np.linalg.inv(x_x_transposed)

stat_beta = x_x_transposed_inverse.dot(stat_x.transpose()).dot(y_with_noise)
print(stat_beta)



# 3 Polynomial Regression

# data generate
bias = 1
beta = np.array([2,3]).reshape(2,1)
noise = np.random.randn(100,1)

x = np.random.randn(100,1)
x_poly = np.hstack([x,x**2])

y = bias + x_poly.dot(beta)
y_with_noise = y+noise

plt.scatter(x,y_with_noise)

# regression

model = LinearRegression()
model.fit(x_poly,y_with_noise)

print(model.intercept_,model.coef_)

pred = model.predict(x_poly)

plt.scatter(x,pred, edgecolors='red')
plt.show()