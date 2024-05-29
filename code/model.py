import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

ecog_data = np.load('ECoG_data.npy')
motion_data = np.load('Motion_data.npy', allow_pickle=True)


def main ():
    X_train, X_test, y_train, y_test = train_test_split(ecog_data, motion_data, test_size=0.2, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)
    print(X_train.shape, "X_Train")
    print(y_train.shape, "y_train")



if __name__ == "__main__":
    main()
    print("finished")