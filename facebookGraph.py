import graphTester2
import graph

data = open('facebook_combined.txt')
lines = data.read().splitlines()
graphData = []

for line in lines:
    graphData.append(line.split())

def createGraph(rawData):
    graph = {}
    for pair in rawData:
        node1 = int(pair[0])
        node2 = int(pair[1])
        if node1 not in graph:
            graph[node1] = set()
        if node2 not in graph:
            graph[node2] = set()
        graph[node1].add(node2)
        graph[node2].add(node1)
    return graph

facebookGraph = graph.Graph(createGraph(graphData))


graphTester2.graphTester(facebookGraph, 4031, 500)
