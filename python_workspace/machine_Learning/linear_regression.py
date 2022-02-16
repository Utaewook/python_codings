from matplotlib import colors
import matplotlib.pylab as plt
from sklearn import linear_model

# reg=linear_model.LinearRegression()

# X = [[174], [152], [138], [128], [186]]
# Y = [71, 55, 46, 38, 88]

# reg.fit(X,Y)

# print(reg.predict([[165]]))
# plt.scatter(X,Y,color='black')

# y_pred=reg.predict(X)

# plt.plot(X,y_pred,color='blue',linewidth=3)
# plt.show()

##Stretch

# reg=linear_model.LinearRegression()

# stretch_time=[[0],[30],[10],[15],[5],[25],[35],[40],[45]]
# n=[4,1,3,2,3,1,0,1,1]
# reg.fit(stretch_time,n)

# n_pred=reg.predict(stretch_time)

# plt.scatter(stretch_time,n,color='black')
# plt.plot(stretch_time,n_pred,color='red',linewidth=2)
# plt.show()

##Birth year

year=[[1930],[1940],[1950],[1965],[1972],[1982],[1992],[2010],[2016]]
life_expectancy=[59,62,70,69,71,74,75,76,78]

reg=linear_model.LinearRegression()
reg.fit(year,life_expectancy)
le_pred=reg.predict(year)

print(reg.predict([[2472]]))

plt.scatter(year,life_expectancy,color='black')
plt.plot(year,le_pred,color='blue',linewidth=2)
plt.show()