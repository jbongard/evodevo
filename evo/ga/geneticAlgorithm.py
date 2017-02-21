from population import POPULATION
import copy

parents = POPULATION(5)

parents.Initialize()

parents.Evaluate(pp=False,pb=True)

print 0,
parents.Print()

for g in range(1,200):

	children = POPULATION(5)

	children.Fill_From(parents)

	children.Evaluate(pp=False,pb=True)

	print g,
	children.Print()

	exit()

#	children.Evaluate(pp=False,pb=True) # 08
#	# children.Print() # 09
#	parents = children
#	print g,
#	parents.Print()
#	# 010 exit(0) 	
#parents.p[0].Start_Evaluation(pp=True,pb=False) # 011
