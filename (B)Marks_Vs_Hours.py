import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

#Dataset
hours=np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
marks=np.array([35,40,45,55,60,75,80,85])

model=LinearRegression()
model.fit(hours,marks)

predicted_marks=model.predict(hours)

new_hours=np.array([[9]])
predicted_new=model.predict(new_hours)

print("Slope (m):",model.coef_[0])
print("Intercept (c):",model.intercept_)
print("Predicted marks for 9 hours :",predicted_new[0])


plt.scatter(hours,marks,color='blue',label="Actual Data")
plt.plot(hours,predicted_marks,color='red',label="Regression Lines")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks(Linear Regression)")
plt.legend()
plt.show()
