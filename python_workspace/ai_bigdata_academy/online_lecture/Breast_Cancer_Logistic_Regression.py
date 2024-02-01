import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functions import *

np.random.seed(2023)

# Data load
print_title("Data load")
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
print(cancer['feature_names'])
print(cancer['target_names'])

data,target = cancer['data'], cancer['target']
print("types of source_data, data, target : ", type(cancer), type(data), type(target))

# data EDA (Extra Data Analysis-탐색적 데이터 분석)
print_title("Data EDA")
df = pd.DataFrame(data, columns=cancer['feature_names'])

print(df.describe())
print(data.shape)
print(pd.Series(target).value_counts())

# histogram으로 target 그리기
plt.hist(target)
plt.show()

# mean radius와 정답간의 상관관계를 plot으로 그림 mean radius가 클 경우 음성에 가까움
plt.scatter(x=data[:,0], y=target)

# 참고로, ndarray의 인덱싱, 슬라이싱의 표현은 다음과 같음
# data[행시작:행끝:간격,열시작:열끝:간격] -> data가 2차원인 경우
# 3차원이상의 경우도 쉼표를 통해 각 차원 배열의 "시작:끝:간격" 으로 접근한다

plt.xlabel('mean radius')
plt.ylabel('target')
plt.show()

# Data split
print_title("Data Split")
from sklearn.model_selection import train_test_split

train_data, test_data, train_target, test_target = train_test_split(data,target,train_size=0.7, random_state=2023)
print("train data length: ", len(train_data))
print("test data length: ", len(test_data))

# Linear Regression으로 학습하면 어떻게 될까?
print_title("Linear Regression")
from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()

# 학습
linear_regressor.fit(train_data,train_target)

# 예측
train_pred_linear = linear_regressor.predict(train_data)
test_pred_linear = linear_regressor.predict(test_data)
print(train_pred_linear[:10]) # 0과 1 사이를 벗어난 음수 값이나 1.5와같은 값이 나옴

# 시각화
fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(10,5))

preds = [
    ("Train", train_data, train_pred_linear),
    ("Test", test_data, test_pred_linear)
]

for idx,(name, d, pred) in enumerate(preds):
    ax = axes[idx]
    ax.scatter(x=d[:,0],y=pred)
    ax.axhline(0,color='red',linestyle='--')
    ax.axhline(1,color='red',linestyle='--')
    ax.set_xlabel('mean radius')
    ax.set_ylabel('predict')
    ax.set_title(f"{name} Data")

plt.show()

# 평가
print_title("Result Validate")
from sklearn.metrics import auc, roc_curve

fpr, tpr, threshold = roc_curve(train_target,train_pred_linear)
auroc = auc(fpr,tpr)
print("fpr",fpr, "tpr",tpr,sep="\n")
print("threshold:",threshold)

# auroc 그리기
plt.plot(fpr,tpr)
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.show()

print(f"AUROC : {auroc:.4f}")

# best threshold 계산
print(np.argmax(tpr-fpr))
J = tpr-fpr
idx = np.argmax(J)
best_thresh = threshold[idx]
print(f"Best Threshold is {best_thresh:.4f}")
print(f"Best Threshold's sensitivity is {tpr[idx]:.4f}")
print(f"Best Threshold's specificity is {1-fpr[idx]:.4f}")
print(f"Best Threshold's J is {J[idx]:.4f}")


# best_threshold는 auroc 그래프에서 직선이 가장 긴 곳
plt.plot(fpr, tpr)
plt.plot(np.linspace(0, 1, 10), np.linspace(0, 1, 10))
plt.plot((fpr[idx], fpr[idx]), (fpr[idx], tpr[idx]), color="red", linestyle="--")
plt.xlabel("fpr")
plt.ylabel("tpr")
plt.show()

# 예측값에 threshold 위치 추가 그리기
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

preds = [
    ("Train", train_data, train_pred_linear),
    ("Test", test_data, test_pred_linear),
]
for idx, (name, d, pred) in enumerate(preds):
    ax = axes[idx]
    ax.scatter(x=d[:,0], y=pred)
    ax.axhline(0, color="red", linestyle="--")
    ax.axhline(1, color="red", linestyle="--")
    ax.set_xlabel("mean_radius")
    ax.set_ylabel("predict")
    ax.set_title(f"{name} Data")
    ax.axhline(best_thresh, color="blue")

plt.show()

# best_threshold로 예측값을 0,1로 변환 후 정확도 확인
train_pred_label = list(map(int,(train_pred_linear>best_thresh)))
test_pred_label = list(map(int,(test_pred_linear>best_thresh)))

from sklearn.metrics import accuracy_score

linear_train_accuracy = accuracy_score(train_target,train_pred_label)
linear_test_accuracy = accuracy_score(test_target,test_pred_label)

print(f"Train accuracy is : {linear_train_accuracy:.2f}")
print(f"Test accuracy is : {linear_test_accuracy:.2f}")

# Logistic Regression
print_title("Logistic Regression")

# logistic regression을 위한 데이터 정규화 (exp 값이 있는데, 값이 클 경우 overflow 가능성 있음)
# Scaling
print_title("Data Scaling")
from sklearn.preprocessing import StandardScaler

# 정규화는 항상 train data를 이용해 학습, valid, test 데이터를 변환
# 모든 데이터를 한번에 학습하는 경우에는, 모델 fitting시 valid및 test data의 분산과 평균이 반영되고
# 이는 overfitting을 일으키는 원인이 됨
scaler = StandardScaler()

scaler.fit(train_data)

# 학습된 scaler로 train/test 데이터를 각각 변환
scaled_train_data = scaler.transform(train_data)
scaled_test_data = scaler.transform(test_data)

print(train_data[0], min(train_data[0]), max(train_data[0]), sep='\n')
print(scaled_train_data[0], min(scaled_train_data[0]), max(scaled_train_data[0]), sep='\n')

# 학습
from sklearn.linear_model import LogisticRegression
logistic_regressor = LogisticRegression()

logistic_regressor.fit(scaled_train_data,train_target)

# 예측
# 분류를 하는 모델의 경우에는 두 가지 방법이 있음
# 1. predict : 해당 데이터가 어떤 클래스에 속할지 바로 알려줌
# 2. predict_proba : 해당 데이터가 각 클래스에 속할 확률을 알려줌

train_pred_logit = logistic_regressor.predict(scaled_train_data)
test_pred_logit = logistic_regressor.predict(scaled_test_data)
train_pred_logit_proba = logistic_regressor.predict_proba(scaled_train_data)
test_pred_logit_proba = logistic_regressor.predict_proba(scaled_test_data)

print(train_pred_logit[:10])
print(train_pred_logit_proba[:10])

# 평가
# 데이터의 AUROC를 계산하기 위해서는 1의 클래스로 분류될 확률만 필요함
# 1에 속할 확률만 남기기


print_title("Evaluate")
train_pred_logit_proba = train_pred_logit_proba[:,1]
test_pred_logit_proba = test_pred_logit_proba[:,1]

print(train_pred_logit_proba[0])

from sklearn.metrics import auc, roc_curve

fpr, tpr, threshold = roc_curve(train_target, train_pred_logit_proba)
auroc = auc(fpr, tpr)

plt.plot(fpr,tpr)
plt.xlabel("fpr")
plt.ylabel("tpr")
plt.show()

print(f"AUROC : {auroc:.4f}")

J = tpr - fpr
idx = np.argmax(J)
best_thresh = threshold[idx]

print(f"Best Threshold is {best_thresh:.4f}")
print(f"Best Threshold's sensitivity is {tpr[idx]:.4f}")
print(f"Best Threshold's specificity is {1-fpr[idx]:.4f}")
print(f"Best Threshold's J is {J[idx]:.4f}")


plt.plot(fpr, tpr)
plt.plot(np.linspace(0, 1, 10), np.linspace(0, 1, 10))
plt.plot((fpr[idx],fpr[idx]), (fpr[idx], tpr[idx]), color="red", linestyle="--")
plt.xlabel("fpr")
plt.ylabel("tpr")
plt.show()

plt.scatter(x=scaled_train_data[:,0], y=train_pred_logit_proba)
plt.axhline(best_thresh, color="blue")
plt.axhline(0, color="red", linestyle="--")
plt.axhline(1, color="red", linestyle="--")
plt.xlabel("mean radius")
plt.ylabel("Probability")
plt.show()


# 예측값을 best_threshold 기준으로 0,1로 변환 한 후 정확도 계산
train_pred_label = list(map(int, (train_pred_logit_proba > best_thresh)))
test_pred_label = list(map(int, (test_pred_logit_proba > best_thresh)))

proba_train_accuracy = accuracy_score(train_target, train_pred_label)
proba_test_accuracy = accuracy_score(test_target, test_pred_label)

print(f"Train accuracy is : {proba_train_accuracy:.2f}")
print(f"Test accuracy is : {proba_test_accuracy:.2f}")

# 예측값으로 정확도 계산
train_accuracy = accuracy_score(train_target, train_pred_logit)
test_accuracy = accuracy_score(test_target, test_pred_logit)

print_title("Result")
print(f"Linear Regression Test Accuracy: {linear_test_accuracy:.2f}")
print(f"Logistic Regression predict_proba Test Accuracy: {proba_test_accuracy:.2f}")
print(f"Logistic Regression predict Test Accuracy: {test_accuracy:.2f}")

# 정확도 계산 결과, linear regression이 0.96정도, logistic regression(proba, non_proba)이 0.98정도로 나옴