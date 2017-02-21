from pyrosim import PYROSIM

sim = PYROSIM( playPaused=True, evalTime=1000 )

sim.Send_Cylinder( objectID = 0 , x=0 , y=0 , z=0.6 , length=1 , radius=0.1 )

sim.Send_Cylinder( objectID = 1 , x=0 , y=0.5, z=1.1, r=1, g=0, b=0, r1=0, r2=1, r3=0)

sim.Send_Joint( firstObjectID = 0 , secondObjectID = 1 , x=0, y=0, z=1.1, n1=1, n2=0, n3=0, lo=-3.14159/2, hi=3.14159/2)

sim.Start()
