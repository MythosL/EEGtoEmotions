import numpy as np
from scipy.stats import multivariate_normal

def differential_entropy(data):
    cov = np.cov(data, rowvar=False)
    return 0.5 * np.log(np.linalg.det(2 * np.pi * np.e * cov))

npzfile = np.load('data.npz')

data = npzfile['data']

entropy = differential_entropy(data)

with open('calculatedentropy.txt', 'w') as f:
    f.write(str(entropy))