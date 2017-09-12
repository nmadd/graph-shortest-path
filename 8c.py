from graph import Graph
from graphTester2 import graphTester

testGraph = Graph()
testGraph.initGraph(1000, .1)

graphTester(testGraph, 1000, 10000)

# 10,000 tests
# ('Average path length', 1.8986)
