from graph import Graph
from graphTester import graphTester

graphSize = 4039

testGraph = Graph()
testGraph.initGraph(graphSize, .0108)

print(graphTester(testGraph, graphSize, 1000, True))

# Results of 10,000 tests:
# Test 1: ('Average path length', 1.8986)
# Test 2: ('Average path length', 1.9018)
