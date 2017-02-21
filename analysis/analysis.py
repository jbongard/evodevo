import matplotlib.pyplot as plt

import numpy as np

import scipy.stats

f = open('../data/evo.txt','r')
e = np.fromfile(f,sep=' ')
f.close()

f = open('../data/devo.txt','r')
d = np.fromfile(f,sep=' ')
f.close()

means = np.zeros(2,dtype='f')
means[0] = np.mean(e)
means[1] = np.mean(d)

sems = np.zeros(2,dtype='f')
sems[0] = scipy.stats.sem(e)
sems[1] = scipy.stats.sem(d) 

print scipy.stats.mannwhitneyu(e,d)

f = plt.figure()
#ax = f.add_subplot(111)

plt.bar([0,1], means, yerr=1.96*sems, color=[0.9,0.9,0.9])

#ax.set_ylim(-2,+2)
plt.show()
