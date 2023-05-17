import numpy as np


dataset = np.genfromtxt("vsirazenzadnji.csv",delimiter=' ')
np.random.shuffle(dataset)
dataset.tofile('randomisedvsirazenzadnji.csv', sep = ' ')


zadnji = np.genfromtxt("zadnji.csv",delimiter=' ')
np.random.shuffle(zadnji)
zadnji.tofile('radnomisedzadnji.csv', sep = ' ')
