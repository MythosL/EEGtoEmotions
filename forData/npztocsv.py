import numpy as np
import pickle

for i in range(1,16):
    with open("csvData/all-1+5x2" + ".csv", "a") as f:
        data_npz = np.load("EEG_DE_features/{}_123.npz".format(i))
        data = pickle.loads(data_npz['data'])
        labels = pickle.loads(data_npz['label'])
        for key, value in data.items():
            # first creating a vector (value) wich cointains all features data
            # then creating a another vector(arr) wich cointains the labels
            arr = np.array(labels[key])
            # reshaping arr into a vertical vector
            arr_reshaped = np.reshape(arr,(len(arr),1))
            solution = np.concatenate((value,arr_reshaped), axis=1)
            np.savetxt(f, solution)

participant = np.genfromtxt("csvData/zadnji.csv",delimiter=' ')
firstfiveemotions = participant[:184]
np.savetxt('csvData/all-1+5x2.csv', firstfiveemotions ,delimiter=' ')



"""with open("csvData/zadnji_eye" + ".csv", "a") as f:
    for i in range(1,2):
        data_npz = np.load("Eye_movement_features/{}_123.npz".format(i))
        data = pickle.loads(data_npz['data'])
        labels = pickle.loads(data_npz['label'])
        for key, value in data.items():
            # first creating a vector (value) wich cointains all features data
            # then creating a another vector(arr) wich cointains the labels
            arr = np.array(labels[key])
            # reshaping arr into a vertical vector
            arr_reshaped = np.reshape(arr,(len(arr),1))
            # merging the two vectors together
            solution = np.concatenate((value,arr_reshaped), axis=1)
            np.savetxt(f, solution)"""