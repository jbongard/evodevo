from pyrosim import PYROSIM

from robot import ROBOT

import random, math, numpy, constants as c

class INDIVIDUAL:

        def __init__(self, i):

		self.ID = i

		self.genome = numpy.random.random([5,8,3]) * 2 - 1

		self.genome[:,:,2] = numpy.random.randint(0,c.evaluationTime,[5,8])

		self.fitness = 0

	def Start_Evaluation(self, env, pp, pb):

        	self.sim = PYROSIM( playPaused = pp, playBlind=pb, evalTime=c.evaluationTime )

        	robot = ROBOT( self.sim , self.genome )

		env.Send_To( self.sim )

        	self.sim.Start()

	def Compute_Fitness(self):

        	self.sim.Wait_To_Finish()

        	sensorData = self.sim.Get_Sensor_Data(sensorID = 4 , s = 0 )

		currentFitness = sensorData[-1]

		if ( currentFitness < self.fitness ):

			self.fitness = currentFitness

        	# self.fitness = self.fitness + currentFitness

		# if ( self.fitness > 10.0 ):

		#	self.fitness = 10.0

		del self.sim

	def Mutate(self):

		s = random.randint(0,4)

		m = random.randint(0,7)

		k = random.randint(0,2)

		if ( k < 2 ):

			self.genome[s,m,k] = random.gauss( self.genome[s,m,k] , math.fabs(self.genome[s,m,k]) )

			if ( self.genome[s,m,k] > 1.0 ):

				self.genome[s,m,k] = 1.0

			if ( self.genome[s,m,k] < -1.0 ):

				self.genome[s,m,k] = -1.0
		else:
			self.genome[s,m,k] = numpy.random.randint(0,c.evaluationTime)

	def Print(self):

		print '[',

		print self.ID,

		print self.fitness,

		print '] ',
