from graph import Graph
from graphTester import graphTester
from facebookGraph import parseFacebookData, createFacebookGraph

facebookGraph = Graph(createFacebookGraph(parseFacebookData('facebook_combined.txt')))

print(graphTester(facebookGraph, 4038, 1000, True))
