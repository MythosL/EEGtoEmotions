import numpy as np

for i in range(1,15):
    participant = np.genfromtxt("{}.csv".format(str(i)),delimiter=' ')
    firstfiveemotions = participant[:184]
    np.savetxt('participant_{}_firstfiveemotions.csv'.format(str(i)), firstfiveemotions ,delimiter=' ')
    otheremotions = participant[183:]
    np.savetxt('participant_{}_otheremotions.csv'.format(str(i)), otheremotions ,delimiter=' ')