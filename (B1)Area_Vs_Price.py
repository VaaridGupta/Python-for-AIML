# Q2:Predict HOuse price vs Area

import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


#Dataset
area=np.array([500,700,900,1100,1300,1500,1700,1900]).reshape(-1,1)
price=np.array([100000,150000,180000,220000,260000,300000,340000,380000])

model=LinearRegression()
model.fit(area,price)

predict_price=model.predict(area)

print("Slope (m):",model.coef_[0])
print("Intercept (c):", model.intercept_)
while True:
    x = float(input("Enter area of house (or -1 to stop): "))
    if x == -1:
        break
    pred = model.predict(np.array([[x]]))[0]
    print("Predicted price:", pred)

plt.scatter(area,price,color='green',label="Actual Data")
plt.plot(area,predict_price,color='brown',label="Regression Line")
plt.xlabel("Area")
plt.ylabel("Price")
plt.legend()
plt.show()

    


                            
