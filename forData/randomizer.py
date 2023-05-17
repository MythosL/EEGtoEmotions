import numpy as np

for i in range (1,15):
  fl = np.genfromtxt("person{}.csv".format(i),delimiter=' ')
  np.random.shuffle(fl)
  fl.tofile("randomisedperson{}.csv".format(o), sep = ' ')
