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

# train_test_split 함수를 통해 데이터를 학습 데이터와 검증 데이터로 나눈다
#  train_test_split(
#     *arrays,
#     test_size=None,
#     train_size=None,
#     random_state=None,
#     shuffle=True,
#     stratify=None,
# )
#
# *arrays: 입력은 array로 이루어진 데이터을 받습니다.
# test_size: test로 분할될 사이즈를 정합니다.
# train_size: train으로 분할될 사이즈를 정합니다.
# random_state: 다음에도 같은 값을 얻기 위해서 난수를 고정합니다
# shuffle: 데이터를 섞을지 말지 결정합니다.
# stratify: 데이터를 나눌 때 정답의 분포를 반영합니다.

train_data, test_data, train_target, test_target = train_test_split(data,target,test_size=0.3)

print("source, train, test data len:",len(data),len(train_data),len(test_data))

print("train ratio : {:.2f}".format(len(train_data)/len(data)))
print("test ratio : {:.2f}".format(len(test_data)/len(data)))


# Linear Regression
print("\n\nLinear_Regression\n")
from sklearn.linear_model import LinearRegression

# 학습
multi_regression = LinearRegression()   # Linear Regression 모델 사용
multi_regression.fit(train_data, train_target) # 모델을 train 데이터와 train 타겟으로 학습시킨다.

# 회귀식 확인
print(multi_regression.intercept_, multi_regression.coef_)  # 학습된 모델의 bias와 coef값 확인

# 예측
pred_train_multi = multi_regression.predict(train_data)
pred_test_multi = multi_regression.predict(test_data)

# 평가
from sklearn.metrics import mean_squared_error

# mean_squared_error를 통해 두 값 차이의 제곱의 평균을 계산한다 -> avg((y-y')^2)
# 값이 작을 수록 예측을 잘한것!

multi_train_mse = mean_squared_error(pred_train_multi, train_target)  # 검증
multi_test_mse = mean_squared_error(pred_test_multi, test_target)  # 평가

print(f"Multi Regression Train MSE is {multi_train_mse:.4f}")
print(f"Multi Regression Test MSE is {multi_test_mse:.4f}")


# Ridge Regression
print("\n\nRidge\n")
from sklearn.linear_model import Ridge

# 학습
ridge_regression = Ridge()
ridge_regression.fit(train_data,train_target)

# 회귀식 확인
print(ridge_regression.intercept_,ridge_regression.coef_)

# 예측
pred_train_ridge = ridge_regression.predict(train_data)
pred_test_ridge = ridge_regression.predict(test_data)


# 평가
ridge_train_mse = mean_squared_error(pred_train_ridge,train_target)
ridge_test_mse = mean_squared_error(pred_test_ridge,test_target)

print(f"Ridge Regression Train MSE is {ridge_train_mse:.4f}")
print(f"Ridge Regression Test MSE is {ridge_test_mse:.4f}")



# LASSO
print("\n\nLASSO\n")
from sklearn.linear_model import Lasso

# 학습
lasso_regressor = Lasso()
lasso_regressor.fit(train_data,train_target)

# 회귀식 확인
print(lasso_regressor.intercept_, lasso_regressor.coef_)

# 예측
pred_train_lasso = lasso_regressor.predict(train_data)
pred_test_lasso = lasso_regressor.predict(test_data)

# 평가
lasso_train_mse = mean_squared_error(pred_train_lasso,train_target)
lasso_test_mse = mean_squared_error(pred_test_lasso,test_target)
print(f"LASSO Regression Train MSE is {lasso_train_mse:.4f}")
print(f"LASSO Regression Test MSE is {lasso_test_mse:.4f}")


# 정리
print("\n\n Results\n")
print(f"Multi Regression Test MSE is {multi_test_mse:.4f}")
print(f"Ridge Regression Test MSE is {ridge_test_mse:.4f}")
print(f"LASSO Regression Test MSE is {lasso_test_mse:.4f}")

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
preds = [
    ("Multi regression", pred_test_multi),
    ("Ridge regression", pred_test_ridge),
    ("LASSO regression", pred_test_lasso),
]

for idx, (name, test_pred) in enumerate(preds):
    ax = axes[idx]
    ax.scatter(test_pred, test_target)
    ax.plot(np.linspace(0, 330, 100), np.linspace(0, 330, 100), color="red")
    ax.set_xlabel("Predict")
    ax.set_ylabel("Real")
    ax.set_title(name)

plt.show()