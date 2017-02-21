from pyrosim import PYROSIM
import math, random

L = 1.0

R = 0.1

sim = PYROSIM( evalTime = 1000 )

# Chassis

sim.Send_Box(objectID=0, x=0, y=+L/4, z=L, length=L/2, width=L/2, height=L/2)

sim.Send_Box(objectID=1, x=0, y=-L/4, z=L, length=L/2, width=L/2, height=L/2, r=1, g = 0 , b = 0)

#Legs

sim.Send_Cylinder(objectID=2, x=L/4, y=L, z=L, r1=0, r2=1, r3=0, length=L, radius=R, r=0, g=1, b=0)

sim.Send_Cylinder(objectID=3, x=-L/4, y=L, z=L, r1=0, r2=1, r3=0, length=L, radius=R, r=0, g=0, b=1)

sim.Send_Cylinder(objectID=4, x=L/4, y=-L, z=L, r1=0, r2=1, r3=0, length=L, radius=R, r=1, g=0, b=1)

sim.Send_Cylinder(objectID=5, x=-L/4, y=-L, z=L, r1=0, r2=1, r3=0, length=L, radius=R, r=0, g=1, b=1)

# Wheels

sim.Send_Cylinder(objectID=6, x=L/4, y=1.5*L, z=L, length=0, radius=1.5*R, r=0, g=0, b=0)

sim.Send_Cylinder(objectID=7, x=-L/4, y=1.5*L, z=L, length=0, radius=1.5*R, r=0, g=0, b=0)

sim.Send_Cylinder(objectID=8, x=L/4, y=-1.5*L, z=L, length=0, radius=1.5*R, r=0, g=0, b=0)

sim.Send_Cylinder(objectID=9, x=-L/4, y=-1.5*L, z=L, length=0, radius=1.5*R, r=0, g=0, b=0)

# Chassis Joint

sim.Send_Joint(jointID=0, firstObjectID=0, secondObjectID=1, x=0, y=0, z=L, n1=0, n2=0, n3=1)

# Chassis to leg joints

sim.Send_Joint(jointID=1, firstObjectID=0, secondObjectID=2, x=L/4, y=L/2, z=L, n1=1, n2=0, n3=0)

sim.Send_Joint(jointID=2, firstObjectID=0, secondObjectID=3, x=-L/4, y=L/2, z=L, n1=1, n2=0, n3=0)

sim.Send_Joint(jointID=3, firstObjectID=1, secondObjectID=4, x=L/4, y=-L/2, z=L, n1=1, n2=0, n3=0)

sim.Send_Joint(jointID=4, firstObjectID=1, secondObjectID=5, x=-L/4, y=-L/2, z=L, n1=1, n2=0, n3=0)

# Leg to wheel joints

sim.Send_Joint(jointID=5, firstObjectID=2, secondObjectID=6, x=L/4, y=1.5*L, z=L, n1=1, n2=0, n3=0)

sim.Send_Joint(jointID=6, firstObjectID=3, secondObjectID=7, x=-L/4, y=1.5*L, z=L, n1=1, n2=0, n3=0)

sim.Send_Joint(jointID=7, firstObjectID=4, secondObjectID=8, x=L/4, y=-1.5*L, z=L, n1=1, n2=0, n3=0)

sim.Send_Joint(jointID=8, firstObjectID=5, secondObjectID=9, x=-L/4, y=-1.5*L, z=L, n1=1, n2=0, n3=0)

# Sensors

sim.Send_Touch_Sensor(sensorID=0, objectID=0)

sim.Send_Touch_Sensor(sensorID=1, objectID=1)

sim.Send_Touch_Sensor(sensorID=2, objectID=6)

sim.Send_Touch_Sensor(sensorID=3, objectID=7)

sim.Send_Touch_Sensor(sensorID=4, objectID=8)

sim.Send_Touch_Sensor(sensorID=5, objectID=9)

# Sensor neurons

for s in range(0,5+1):

	sim.Send_Sensor_Neuron(neuronID=s, sensorID=s)

# Motor neurons

for j in range(0,8+1):

	sim.Send_Motor_Neuron(neuronID = 4+j , jointID = j)

# Synapses

for s in range(0,5+1):

	for m in range(4,12+1):

		sim.Send_Synapse(sourceNeuronID = s , targetNeuronID = m , weight = random.random()*2-1)

sim.Start()

