class ROBOT:

        def __init__(self, sim, wts):

		sim.Send_Cylinder( objectID = 0 , x=0 , y=0 , z=0.6 , length=1 , radius=0.1 )

		sim.Send_Cylinder( objectID = 1 , x=0 , y=0.5, z=1.1, r=1, g=0, b=0, r1=0, r2=1, r3=0)

		sim.Send_Joint( jointID = 0 , firstObjectID = 0 , secondObjectID = 1 , x=0, y=0, z=1.1, n1=-1, n2=0, n3=0, lo=-3.14159/2, hi=3.14159/2)

		sim.Send_Touch_Sensor(sensorID = 0 , objectID = 0)

		sim.Send_Touch_Sensor(sensorID = 1 , objectID = 1)

		sim.Send_Proprioceptive_Sensor(sensorID=2, jointID=0)

		sim.Send_Ray_Sensor(sensorID = 3 , objectID = 1 , x = 0 , y = 1.1 , z = 1.1 , r1 = 0 , r2 = 1, r3 = 0)

		sim.Send_Position_Sensor(sensorID=4, objectID = 1)

		for s in range(0,3+1):

			sim.Send_Sensor_Neuron(neuronID=s, sensorID=s )

		sim.Send_Motor_Neuron(neuronID=4 , jointID=0 )

		for s in range(0,3+1):

			sim.Send_Synapse(sourceNeuronID = s , targetNeuronID = 4 , weight = wts[s] )
