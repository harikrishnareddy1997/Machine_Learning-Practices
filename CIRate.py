import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model as lnrg

data = pd.read_csv('CIdata2.csv',low_memory=False,nrows=390)
# print(data)
# data.head()
x=data[['Amount','rate']]
y=data['Amount1']
# x=data[['amount','rate']]
# y=data['interest']
rgr=lnrg.LinearRegression()
rgr.fit(x,y)
print(rgr.intercept_)
print(rgr.coef_)
i=np.array([[3000.0,2.5]])
print(rgr.predict(i))
plt.xlabel("Amount Taken")
plt.ylabel("Intrst Paid")
plt.scatter(data['Amount'],data['Amount1'],marker="x")
plt.scatter(i[0][0], rgr.predict(i), s=100)
plt.plot(np.sort(data['Amount']),np.sort(rgr.predict(x)))
plt.show()