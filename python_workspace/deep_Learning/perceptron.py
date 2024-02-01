from numpy.core.fromnumeric import argmax
from sklearn.linear_model import Perceptron
from sklearn.utils.extmath import weighted_mode

X=[[0,0],[0,1],[1,0],[1,1]]
y=[0,0,0,1]

weights=[0.0,0.0]
bias=0.0

clf=Perceptron(tol=1e-3, random_state=0)

clf.fit(X,y)

def calculate(input):
    global weights
    global bias
    acvitation=bias
    
    for i in range(2):
        acvitation+=weights[i]*input[i]
        if acvitation>=0.0:
            return 1.0
        else:
            return 0.0
    
def train_weights(X,y,l_rate,n_epoch):
    global weights
    global bias
    for epoch in range(n_epoch):
        sum_error=0.0
        for row, target in zip(X,y):
            actual=calculate(row)
            error=target-actual
            bias=bias+l_rate*error
            sum_error+=error**2
            for i in range(2):
                weights[i]=weights[i]+l_rate*error*row[i]
            print(weights,bias)
        print('에포크 번호=%d, 학습률=%.3f, 오류=%.3f'%(epoch,l_rate,sum_error))
    return weights

l_rate=0.1
n_epoch=5
weights=train_weights(X,y,l_rate,n_epoch)
print(weights,bias)
            