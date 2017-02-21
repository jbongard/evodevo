import constants as c

class ENVIRONMENT:

        def __init__(self, e): 

		self.ID = e

		self.l = c.l
		self.w = c.l
		self.h = c.l

		self.z = c.l/2
 
		if ( self.ID == 0 ):

			self.Place_Light_Source_To_The_Front()

		elif ( self.ID == 1 ):

                        self.Place_Light_Source_To_The_Right()

                elif ( self.ID == 2 ):

                        self.Place_Light_Source_To_The_Back()
		else:
                        self.Place_Light_Source_To_The_Left()

		# print self.l, self.w, self.h, self.x, self.y, self.z

	def Place_Light_Source_To_The_Back(self):

		self.x = 0

		self.y = -30 * c.l

        def Place_Light_Source_To_The_Front(self):

                self.x = 0

                self.y = 30 * c.l

        def Place_Light_Source_To_The_Left(self):

                self.x = -30 * c.l

                self.y = 0

        def Place_Light_Source_To_The_Right(self):

                self.x = 30 * c.l

                self.y = 0 

	def Send_To(self,sim):

		sim.Send_Box(objectID=9, x=self.x, y=self.y, z=self.z, length=self.l, width=self.w, height=self.h, r=1, g=1, b=1)

		sim.Send_Light_Source(objectIndex = 9)

