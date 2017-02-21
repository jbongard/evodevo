from pyrosim import PYROSIM

from robot import ROBOT

import random

for i in range(0,10):

	sim = PYROSIM( playPaused=False, evalTime=200 )

	robot = ROBOT( sim , random.random()*2 - 1 )

	sim.Start()

	sim.Wait_To_Finish()

#f = plt.figure()
#ax = f.add_subplot(111)
#plt.plot(sensorData)
#ax.set_ylim(-2,+2)
#plt.show()

