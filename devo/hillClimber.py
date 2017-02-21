from individual import INDIVIDUAL

import copy , pickle

# ----------------------

parent = INDIVIDUAL()

parent.Evaluate(True)

print parent.fitness

for g in range(0,200):

	child = copy.deepcopy( parent )

	child.Mutate()

	child.Evaluate(True)

        print '[g:' , g , ']',

        print '[pw:' , parent.genome , ']',

	print '[p:' , parent.fitness , ']',

	print '[c:' , child.fitness , ']'

	if ( child.fitness > parent.fitness ):

		parent = child

		f = open('robot.p','w')

		pickle.dump(parent , f )

		f.close()

parent.Evaluate(False)


