import constants as c

class ROBOT:

        def __init__(self, sim, wts):

		self.Send_Objects(sim)

		self.Send_Joints(sim)

		self.Send_Sensors(sim)

		self.Send_Neurons(sim)

		self.Send_Synapses(sim,wts)

	def Send_Objects(self,sim):

		sim.Send_Box(objectID = 0 , x=0, y=0, z=c.l+c.r, length=c.l, width=c.l, height=2*c.r, r=0.5, g=0.5, b=0.5)

		sim.Send_Cylinder( objectID = 1 , x=0, y=c.l, z=c.l+c.r, length=c.l, radius=c.r, r1=0, r2=1, r3=0, r=0.5, g=0, b=0)

                sim.Send_Cylinder( objectID = 2 , x=c.l, y=0, z=c.l+c.r, length=c.l, radius=c.r, r1=1, r2=0, r3=0, r=0, g=0.5, b=0)

		sim.Send_Cylinder( objectID = 3, x=0, y=-c.l, z=c.l+c.r, length=c.l, radius=c.r, r1=0, r2=-1, r3=0, r=0, g=0, b=0.5)

		sim.Send_Cylinder( objectID = 4, x=-c.l, y=0, z=c.l+c.r, length=c.l, radius=c.r, r1=-1, r2=0, r3=0, r=0.5, g=0, b=0.5)

		sim.Send_Cylinder( objectID = 5, x=0, y=3*c.l/2, z=c.l/2+c.r, length=c.l, radius=c.r, r=1, g=0, b=0)

		sim.Send_Cylinder( objectID = 6, x=3*c.l/2, y=0, z=c.l/2+c.r, length=c.l, radius=c.r, r=0, g=1, b=0)

		sim.Send_Cylinder( objectID = 7, x=0, y=-3*c.l/2, z=c.l/2+c.r, length=c.l, radius=c.r, r=0, g=0, b=1)

		sim.Send_Cylinder( objectID = 8, x=-3*c.l/2, y=0, z=c.l/2+c.r, length=c.l, radius=c.r, r=1, g=0, b=1)

	def Send_Joints(self,sim):

		sim.Send_Joint( jointID = 0 , firstObjectID = 0 , secondObjectID = 1, x=0, y=c.l/2,   z=c.l+c.r, n1=-1, n2=0, n3=0,  lo=-3.14159/2, hi=3.14159/2)

		sim.Send_Joint( jointID = 1 , firstObjectID = 1 , secondObjectID = 5, x=0, y=3*c.l/2, z=c.l+c.r, n1=-1, n2=0, n3=0,  lo=-3.14159/2, hi=3.14159/2)

                sim.Send_Joint( jointID = 2 , firstObjectID = 0 , secondObjectID = 2, x=c.l/2, y=0,   z=c.l+c.r, n1=0, n2=+1, n3=0,  lo=-3.14159/2, hi=3.14159/2)

                sim.Send_Joint( jointID = 3 , firstObjectID = 2 , secondObjectID = 6, x=3*c.l/2, y=0, z=c.l+c.r, n1=0, n2=+1, n3=0,  lo=-3.14159/2, hi=3.14159/2)

                sim.Send_Joint( jointID = 4 , firstObjectID = 0 , secondObjectID = 3, x=0, y=-c.l/2,   z=c.l+c.r, n1=1, n2=0, n3=0,  lo=-3.14159/2, hi=3.14159/2)

                sim.Send_Joint( jointID = 5 , firstObjectID = 3 , secondObjectID = 7, x=0, y=-3*c.l/2, z=c.l+c.r, n1=1, n2=0, n3=0,  lo=-3.14159/2, hi=3.14159/2)

                sim.Send_Joint( jointID = 6 , firstObjectID = 0 , secondObjectID = 4, x=-c.l/2, y=0,   z=c.l+c.r, n1=0, n2=-1, n3=0, lo=-3.14159/2, hi=3.14159/2)

                sim.Send_Joint( jointID = 7 , firstObjectID = 4 , secondObjectID = 8, x=-3*c.l/2, y=0, z=c.l+c.r, n1=0, n2=-1, n3=0, lo=-3.14159/2, hi=3.14159/2)

	def Send_Sensors(self,sim):

		for t in range(0,3+1):

			sim.Send_Touch_Sensor(sensorID = t , objectID = 5+t)

		sim.Send_Position_Sensor(sensorID=4, objectID = 0)

	def Send_Neurons(self,sim):

		for s in range(0,3+1):

			sim.Send_Sensor_Neuron(neuronID=s, sensorID=s )

		for m in range(0,7+1):

			sim.Send_Motor_Neuron(neuronID=4+m , jointID=m , tau=0.3)

	def Send_Synapses(self,sim,wts):

		for s in range(0,3+1):

			for m in range(0,7+1):

				sim.Send_Synapse(sourceNeuronID = s , targetNeuronID = 4+m , weight = wts[s,m] )

