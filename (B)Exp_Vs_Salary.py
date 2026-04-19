#Q1:Predict salary based on years of experience.

import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

#Dataset
exp=np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
salary=np.array([25000,30000,35000,40000,45000,50000,55000,60000])

model=LinearRegression()
model.fit(exp,salary)

predict_salary=model.predict(exp)
new_exp=np.array([9,25,15]).reshape(-1,1)
predicted_new=model.predict(new_exp)

print("Predicted New Salaries are :",predicted_new)
print("Slope (m):",model.coef_[0])
print("Intercept (c):",model.intercept_)

plt.scatter(exp,salary,color='purple',label='Actual Data')
plt.plot(exp,predict_salary,color='yellow',label='Regression Line')
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()
