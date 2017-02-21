from population import POPULATION
import copy

parents = POPULATION(10)

parents.Initialize() # 09

parents.Evaluate(pp=False,pb=True)

parents.Print()

for g in range(1,200):
	children = copy.deepcopy(parents)
	children.Mutate()
	children.Evaluate(pp=False,pb=True)
	parents.ReplaceWith(children)
	#parents.Sort()
	print g,
	parents.Print()

parents.Evaluate(pp=True,pb=False)

