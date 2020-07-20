
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Reading the data

dataset_train_x = pd.read_csv('sound_x_train_big.csv')
training_set_x = dataset_train_x.iloc[:, 0:1].values

dataset_train_y = pd.read_csv('sound_y_train_big.csv')
training_set_y = dataset_train_y.iloc[:, 0:1].values

print(training_set_x)

# Feature scaling

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0,1))
training_set_scaled_x = sc.fit_transform(training_set_x)
training_set_scaled_y = sc.transform(training_set_y)

# Using the data of last 60 instances to predict the next instance
X_train = []
y_train = []
for i in range(60, len(training_set_x)):
  X_train.append(training_set_scaled_x[i-60:i, 0])
  y_train.append(training_set_scaled_y[i, 0])

X_train = np.array(X_train)
y_train = np.array(y_train)

print(X_train.shape)


# Refroming the data for inputting
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1],1))

print(X_train.shape)

print(y_train)
print(y_train.shape)

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

# Creating th model structure
regressor = Sequential()
regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))
regressor.add(Dense(units = 1))

regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Feeding the data into the model
regressor.fit(X_train, y_train, batch_size = 32, epochs = 2)

# Reading the test data
dataset_test_x = pd.read_csv('sound_x_test_big.csv')
dirty_audio = dataset_test_x.iloc[:, 0:1].values

dirty_audo =sc.transform(dirty_audio)

X_test = []
for i in range(0,len(dirty_audio)-60):
  X_test.append(dirty_audio[i:i+60, 0])

X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Prediting on the test data
predicted_audio = regressor.predict(X_test)

predicted_audio = sc.inverse_transform(predicted_audio)

clean_audio_dataset_test = pd.read_csv('sound_y_test_big.csv')
clean_audio = clean_audio_dataset_test.iloc[:, 0:1]

# Plotting the real and predicted values
plt.plot(clean_audio, color = 'red', label = 'Actual clean audio')
plt.plot(predicted_audio, color = 'blue', label = 'Predicted Clean Audio')
plt.title('Audio Clean')
plt.xlabel('Time')
plt.ylabel('Audio Features')
plt.legend()
plt.show()


# Data paddding (Maybe required)
# temp = predicted_audio
# print(temp.shape)
# for i in range(60):
#   temp = np.append(temp, [[0]], 0)