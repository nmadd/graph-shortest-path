from graph import Graph
from graphTester import graphTester

graphSize = 1000
probability = .1
numberOfTests = 10000
executionTrace = True

testGraph = Graph()
testGraph.initGraph(graphSize, probability)

print(graphTester(testGraph, graphSize, numberOfTests, executionTrace))

# Results of 10,000 tests:
# Test 1: ('Average path length', 1.8986)
# Test 2: ('Average path length', 1.9018)
