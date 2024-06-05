import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Reshape
import matplotlib.pyplot as plt
from tensorflow.keras import regularizers
from tensorflow.keras.optimizers import Adam


if __name__ == '__main__':
    ecog_signals = np.load('ECoG_data.npy')
    motion_signals = np.load('Motion_data.npy')


    X_train, X_temp, y_train, y_temp = train_test_split(ecog_signals, motion_signals, test_size=0.2, shuffle=False)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, shuffle=False)


    

    model = Sequential([
        Dense(units=32, activation='relu'),
        Dropout(0.2),
        Dense(units=32, activation='relu'),
        Dropout(0.2),
        Dense(units=(y_train.shape[1] * y_train.shape[2]),  kernel_regularizer=regularizers.l2(0.01)), 
        Reshape((6,3))
    ])

    optimizer = Adam(learning_rate=0.0001)
    
    model.compile(loss='mse', optimizer=optimizer)
    history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))

    loss = model.evaluate(X_test, y_test)
    print("Test Loss:", loss)



   