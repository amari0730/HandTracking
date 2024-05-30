import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Reshape
import matplotlib.pyplot as plt


if __name__ == '__main__':
    ecog_signals = np.load('ECoG_data.npy')
    motion_signals = np.load('Motion_data.npy')


    X_train, X_temp, y_train, y_temp = train_test_split(ecog_signals, motion_signals, test_size=0.2, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    model = Sequential([
        Dense(units=128, input_shape=(X_train.shape[1],), activation='relu'),
        Dense(units=64, activation='relu'),
        Dense(units=(y_train.shape[1] * y_train.shape[2])), 
        Reshape((6,3))
    ])
    
    model.compile(loss='mean_squared_error', optimizer='adam')
    history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_val, y_val))

    loss = model.evaluate(X_test, y_test)
    print("Test Loss:", loss)

