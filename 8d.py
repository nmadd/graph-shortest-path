from graph import Graph
from graphTester2 import graphTester

nums = [.01, .02, .03, .04, .05, .1, .15, .2, .25, .3, .35, .4, .45, .5]
for num in nums:
    testGraph = Graph()
    testGraph.initGraph(1000, num)
    graphTester(testGraph, 1000, 1000)

# 10,000 tests
# ('Average path length', 0.01, 3.2585947679663225)
# ('Average path length', 0.02, 2.3852)
# ('Average path length', 0.03, 2.1117)
# ('Average path length', 0.04, 1.9851)
# ('Average path length', 0.05, 1.9328)
# ('Average path length', 0.1, 1.8577)
# ('Average path length', 0.15, 1.7858)
# ('Average path length', 0.2, 1.7167)
# ('Average path length', 0.25, 1.6495)
# ('Average path length', 0.3, 1.588)
# ('Average path length', 0.35, 1.5283)
# ('Average path length', 0.4, 1.4834)
# ('Average path length', 0.45, 1.4271)
# ('Average path length', 0.5, 1.3762)
