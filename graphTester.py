import graph
import random

# run shortest path algorithm x amount of times
def graphTester(graph_size, graph_probability, number_of_tests):
    testGraph = graph.Graph()
    testGraph.initGraph(graph_size, graph_probability)
    pathLengths = []
    for i in range(0, number_of_tests):
        # generate random nodes
        node1 = int(random.random() * graph_size) + 1
        node2 = int(random.random() * graph_size) + 1
        # run bfs algo with the random pair of nodes
        shortest_path = testGraph.bfs(node1, node2)
        # watch out for 'infinite' path lengths
        if type(shortest_path) == int:
            pathLengths.append(shortest_path)
        # execution trace
        # if(i < 100 and i < number_of_tests):
        #         print("Node A: ", node1, "Node B: ", node2, "Path length: ", shortest_path)


    # calculate average path length
    avgPathLength = sum(pathLengths) / float(len(pathLengths))
    print('Average path length', graph_probability, avgPathLength)
