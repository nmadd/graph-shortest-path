from graph import Graph
from graphTester2 import graphTester
from facebookGraph import parseFacebookData, createFacebookGraph

facebookGraph = Graph(createFacebookGraph(parseFacebookData('facebook_combined.txt')))

graphTester(facebookGraph, 4038, 100)