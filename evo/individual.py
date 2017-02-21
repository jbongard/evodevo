from pyrosim import PYROSIM

from robot import ROBOT

import random, math, numpy, constants

class INDIVIDUAL:

        def __init__(self, i):

		self.ID = i

		self.genome = numpy.random.random([5,8]) * 2 - 1

		self.fitness = 0

	def Start_Evaluation(self, env, pp, pb):

        	self.sim = PYROSIM( playPaused = pp, playBlind=pb, evalTime=constants.evaluationTime )

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

		self.genome[s,m] = random.gauss( self.genome[s,m] , math.fabs(self.genome[s,m]) )

		if ( self.genome[s,m] > 1.0 ):

			self.genome[s,m] = 1.0

		if ( self.genome[s,m] < -1.0 ):

			self.genome[s,m] = -1.0

	def Print(self):

		print '[',

		print self.ID,

		print self.fitness,

		print '] ',
