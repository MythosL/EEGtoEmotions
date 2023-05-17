import numpy as np
import pickle

for b in range(1,17):
    with open("participant_all-{}+first5x16".format(b) + ".csv", "a") as f:
        for i in range(1,b):
            data_npz = np.load("EEG_DE_features/{}_123.npz".format(i))
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
                np.savetxt(f, solution)
        for i in range(b+1,17):
            data_npz = np.load("EEG_DE_features/{}_123.npz".format(i))
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
                np.savetxt(f, solution)
        data_npz = np.load("EEG_DE_features/{}_123.npz".format(b))
        data = pickle.loads(data_npz['data'])
        labels = pickle.loads(data_npz['label'])
        for b in range(1,17):
             for i in range(0,5):
                # first creating a vector (value) wich cointains all features data
                # then creating a another vector(arr) wich cointains the labels
                arr = np.array(labels[i])
                # reshaping arr into a vertical vector
                arr_reshaped = np.reshape(arr,(len(arr),1))
                # merging the two vectors together
                solution = np.concatenate((data[i],arr_reshaped), axis=1)
                np.savetxt(f, solution)