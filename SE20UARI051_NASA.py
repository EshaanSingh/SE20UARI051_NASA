import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv('nasa_rul.csv')

# Split the data into training and test sets
X_train = data.drop('RUL', axis=1)[:int(0.8 * len(data))]
y_train = data['RUL'][:int(0.8 * len(data))]
X_test = data.drop('RUL', axis=1)[int(0.8 * len(data)):]
y_test = data['RUL'][int(0.8 * len(data)):]

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print('RMSE:', rmse)