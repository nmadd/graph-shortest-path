import graph
import random

# run shortest path algorithm x amount of times
def graphTester(input_graph, graph_size, number_of_tests):
    pathLengths = []
    for i in range(0, number_of_tests):
        # generate random nodes
        node1 = int(random.random() * graph_size) + 1
        node2 = int(random.random() * graph_size) + 1
        # run bfs algo with the random pair of nodes
        if node1 in input_graph.getGraph() and node2 in input_graph.getGraph():
            shortest_path = input_graph.bfs(node1, node2)
        else:
            continue
        # watch out for 'infinite' path lengths
        if type(shortest_path) == int:
            pathLengths.append(shortest_path)
        # execution trace
        # if(i < 100 and i < number_of_tests):
        #         print(i, " Node A: ", node1, "Node B: ", node2, "Path length: ", shortest_path)


    # calculate average path length
    avgPathLength = sum(pathLengths) / float(len(pathLengths))
    print('Average path length', avgPathLength)
