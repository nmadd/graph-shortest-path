from graph import Graph
from graphTester import graphTester

testGraph = Graph()
testGraph.initGraph(1000, .1)

print(graphTester(testGraph, 1000, 1000, True))

# Results of 10,000 tests:
# Test 1: ('Average path length', 1.8986)
# Test 2: ('Average path length', 1.9018)
