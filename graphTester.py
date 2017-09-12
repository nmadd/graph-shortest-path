import graph
import random

# run shortest path algorithm x amount of times
def graphTester(input_graph, graph_size, number_of_tests, execution_trace_flag=False):
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
        # execution trace (if optional flag == True)
        if execution_trace_flag == True:
            if(i < 100 and i < number_of_tests):
                    print "{}) Node A: {}, Node B: {}, Shortest path: {}".format(i + 1, node1, node2, shortest_path)


    # calculate average path length
    avgPathLength = sum(pathLengths) / float(len(pathLengths))
    return 'Average path length: {}'.format(avgPathLength)
