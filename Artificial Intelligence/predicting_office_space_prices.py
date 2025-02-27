# Enter your code here. Read input from STDIN. Print output to STDOUT

features , rows = input().split(' ')
features = int(features)
rows = int(rows)

x=[]
y=[]

for i in range(rows):
    data = input()
    fe = data.split(' ')
    new_data = []
    for i in range(len(fe)-1):
        new_data.append(float(fe[i]))
    x.append(new_data)
    y.append(fe[features])
    # print(new_data, "dependent :",fe[features])
''' 
for i in range(len(x))   :
    print(f"x values {x[i]} fro which y is {y[i]}")
'''

n_x = int(input())
new_X = []
for i in range(n_x):
    new_fe = input()
    data2 = new_fe.split(' ')
    new_data2 = []
    for j in range(len(data2)):
        new_data2.append(float(data2[j]))
            
    new_X.append(new_data2) 


'''
for i in range(len(new_X)):
    print(new_X[i])
'''

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import numpy as np

model = Pipeline([
    ('polynomial',PolynomialFeatures(degree=3)),
    ('model',LinearRegression())
])


model.fit(x,y)

yhat = model.predict(new_X)

for i in range(len(yhat)):
    print(np.round(yhat[i],2))



