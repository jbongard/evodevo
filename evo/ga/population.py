from individual import INDIVIDUAL

import copy, random

class POPULATION:

        def __init__(self,popSize):

		self.p = {}

		self.popSize = popSize

		# 01 Initialize

	def Collect_Children_From(self,other):

		for j in range(1,self.popSize):

			# self.p[j] = copy.deepcopy( other.p[j] ) # 05

			# 06 self.p[j] = copy.deepcopy( other.p[j] ) # 06

			winner = other.Winner_Of_Tournament_Selection()

			self.p[j] = copy.deepcopy( winner ) 

			self.p[j].Mutate() # 07

	def Winner_Of_Tournament_Selection(other):

		i1 = random.randint(0,other.popSize-1)

		i2 = random.randint(0,other.popSize-1)

		while ( i2 == i1 ):

			i2 = random.randint(0,other.popSize-1)

		if ( other.p[i1].fitness > other.p[i2].fitness ):

			return other.p[i1]
		else:
			return other.p[i2]

	def Copy_Best_From(self,other):

		i = other.Find_Best_Individual()

		self.p[0] = copy.deepcopy( other.p[i] )

	def Evaluate(self,pp,pb):

                for i in range(0,self.popSize):

			self.p[i].Start_Evaluation(pp,pb)

                for i in range(0,self.popSize):

			self.p[i].Compute_Fitness()

	def Fill_From(self , other):

		# 02

		# for j in range(0,self.popSize):

		#	self.p[j] = copy.deepcopy( other.p[j] )

		self.Copy_Best_From(other) # 03

		self.Collect_Children_From(other) # 04	

	def Find_Best_Individual(self):

		bestFitness = -1000.0

		bestIndex = -1

		for i in range(0,self.popSize):

			if ( self.p[i].fitness > bestFitness ):

				bestFitness = self.p[i].fitness

				bestIndex = i

		return bestIndex
			
        def Initialize(self):

                for i in range(0,self.popSize):

                        self.p[i] = INDIVIDUAL(i)

	def Mutate(self):

                for i in range(0,self.popSize):

			self.p[i].Mutate()

	def Print(self):

                for i in range(0,self.popSize):

			if ( i in self.p ):

				self.p[i].Print()

		print

	def ReplaceWith(self,other):

                for i in range(0,self.popSize):

			if ( other.p[i].fitness > self.p[i].fitness ):

				self.p[i] = other.p[i]

	def Sort(self):

		for i in range(0,self.popSize-1):

			for j in range(i+1,self.popSize):

				if ( self.p[i].fitness < self.p[j].fitness ):

					tmp = self.p[i]

					self.p[i] = self.p[j]

					self.p[j] = tmp 
