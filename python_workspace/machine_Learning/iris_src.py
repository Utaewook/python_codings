from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

classes={0:'setosa',1:'versicolor',2:'verginica'}
new = [[3,4,5,2],
       [5,4,2,2]]

iris=load_iris()
# print(iris.feature_names)

X=iris.data
Y=iris.target

# print(X)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42,stratify=Y,test_size=0.2)
# print(X_train.shape)
# print(X_test.shape)

knn=KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train,Y_train)
# print(knn.score(X_test,Y_test))

new_predict=knn.predict(new)
print(classes[new_predict[0]])
print(classes[new_predict[1]])