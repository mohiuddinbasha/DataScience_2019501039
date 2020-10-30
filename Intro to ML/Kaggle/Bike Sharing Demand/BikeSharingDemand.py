'''
Bike Sharing Demand

'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

print(train_data.head())
print()
print(train_data.info())
print()
print(train_data.isnull().sum())
# casual and registered columns are not present in test data so they are not useful
train_data.drop(['casual','registered'],axis=1,inplace=True)
print(train_data.head())
# Conversion of datetime type from object to datetime
train_data['datetime'] = pd.to_datetime(train_data['datetime'])
test_data['datetime'] = pd.to_datetime(test_data['datetime'])
print(train_data.info())
#Splitting datetime to day, month, year and hour; Add these as new features to the data set
train_data['year'] = train_data['datetime'].dt.year
train_data['month'] = train_data['datetime'].dt.month
train_data['hour'] = train_data['datetime'].dt.hour
train_data['DayOfWeek'] = train_data['datetime'].dt.dayofweek

test_data['year'] = test_data['datetime'].dt.year
test_data['month'] = test_data['datetime'].dt.month
test_data['hour'] = test_data['datetime'].dt.hour
test_data['DayOfWeek'] = test_data['datetime'].dt.dayofweek

print(train_data.head())
print(test_data.head())
# Selection of features
X_select_train = train_data[['season','holiday','workingday','weather','temp','atemp','humidity','windspeed','year','month','hour','DayOfWeek']]
y_select_train = train_data['count']

X_test = test_data[['season','holiday','workingday','weather','temp','atemp','humidity','windspeed','year','month','hour','DayOfWeek']]

# Splitting of train_data in to training data and validating data
X_train, X_valid, y_train, y_valid = train_test_split(X_select_train, y_select_train, test_size = 0.3, random_state = 42)
print(X_train.head())
print(X_valid.head())

#Calculating Root Mean Squared Logarthimic Error (RMSLE)
def RMSLE(prediction, original):
    print(prediction)
    prediction_processed = prediction.clip(0)
    rmsle = np.sqrt(np.mean(np.array(np.log(prediction_processed + 1) - np.log(original + 1))**2))
    return rmsle

#Linear Regression Model
linearRegressor = LinearRegression()
linearRegressor.fit(X_train,y_train)
y_train_predicted = linearRegressor.predict(X_valid)
print(RMSLE(y_train_predicted, y_valid))

#Plotting between predicted vs original datasets
fig, ax = plt.subplots()
ax.scatter(y_valid, y_train_predicted, s=2)
ax.plot([y_valid.min(), y_valid.max()], [y_valid.min(), y_valid.max()], 'k--', color = 'r', lw=2)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')

# Ridge Regression Model
RidgeRegressor = Ridge()
RidgeRegressor.fit(X_train,y_train)
y_train_predicted_Ridge = RidgeRegressor.predict(X_valid)
print(RMSLE(y_train_predicted_Ridge, y_valid))

#Plotting between predicted vs original datasets
fig, ax = plt.subplots()
ax.scatter(y_valid, y_train_predicted_Ridge, s=2)
ax.plot([y_valid.min(), y_valid.max()], [y_valid.min(), y_valid.max()], 'k--', color = 'r', lw=2)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')

# Random Forest Regression Model
RFR = RandomForestRegressor(n_estimators = 500, min_samples_leaf = 5, random_state = 42)
RFR.fit(X_train,y_train)
y_train_predicted_RFR = RFR.predict(X_valid)
print(RMSLE(y_train_predicted_RFR, y_valid))

#Plotting between predicted vs original datasets
fig, ax = plt.subplots()
ax.scatter(y_valid, y_train_predicted_RFR, s=2)
ax.plot([y_valid.min(), y_valid.max()], [y_valid.min(), y_valid.max()], 'k--', color = 'r', lw=2)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()

# Linear Regression Model on test set
sample_submission = pd.read_csv('sampleSubmission.csv')
predicted_count_LR = linearRegressor.predict(X_test)
sample_submission['count'] = pd.Series(predicted_count_LR.clip(0))
sample_submission.to_csv('Output.csv', index = False)

# Random Forest Regression Model on test set
sample_submission1 = pd.read_csv('sampleSubmission.csv')
predicted_count_RFR = RFR.predict(X_test)
sample_submission1['count'] = pd.Series(predicted_count_RFR.clip(0))
sample_submission1.to_csv('OutputRFR.csv', index = False)