import numpy as np
import scipy.io
from scipy.signal import resample



def main():
    #Load ECoG data
    ecog_data = []
    for i in range(1,65):
        mat = scipy.io.loadmat(f'data/ECoG_ch{i}.mat')
        ecog_data.append(mat[f'ECoGData_ch{i}'].flatten())

    #Convert to numpy array and transpose to get shape (n_samples, n_channels)
    ecog_data = np.array(ecog_data).T


    # Load ECoG time data
    ecog_time = scipy.io.loadmat('data/ECoG_time.mat')['ECoGTime'].flatten()

    # Load motion data
    motion_data = scipy.io.loadmat('data/Motion.mat')['MotionData']
    motion_time = scipy.io.loadmat('data/Motion.mat')['MotionTime'].flatten()

    # Resample ECoG data to match motion data frequency (120 Hz)
    n_samples = len(motion_time)
    ecog_data_resampled = resample(ecog_data, n_samples)
    ecog_time_resampled = np.linspace(ecog_time[0], ecog_time[-1], n_samples)

    # Save the ECoG data
    np.save('ECoG_data.npy', ecog_data_resampled)

    # Save the motion data
    np.save('Motion_data.npy', motion_data)


if __name__ == '__main__':
    data_path = "../data"
    main()