import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

data=pd.read_csv(r"D:\sales_data.csv")

X=data[['Month']]
Y=data['Sales']

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42)

model=LinearRegression()
model.fit(X_train,Y_train)

Y_pred= model.predict(X_test)

#accuracy metrics

r2=r2_score(Y_test,Y_pred)
mae=mean_absolute_error(Y_test,Y_pred)
mse=mean_squared_error(Y_test,Y_pred)

print("R2 score:",r2)
print("Mean Absolute Error:",mae)
print("Mean Squared Error :",mse)

future_months=np.array([13,14,15]).reshape(-1,1)
future_sales=model.predict(future_months)
print("\nFuture Predictions:")

for i,val in enumerate(future_sales):
    print(f"Month{13+i}:{val:.2f}")


plt.scatter(X,Y,color='Black',label='Actual Data')
plt.plot(X,model.predict(X),color="Grey",label="Regression Line")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()

plt.scatter(future_months,future_sales,color='orange',label="Predicted Data")
plt.plot(future_months,future_sales,color='Green',label="Regression Line")
plt.xlabel("Future Months")
plt.ylabel("Fututre Sales")
plt.legend()

