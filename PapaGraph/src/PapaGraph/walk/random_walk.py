from PapaGraph.PapaGraph.PapaGraph import PapaGraph
from PapaGraph.algorithm.shortest_path import steps_from
from PapaGraph.sample.handmande import handmade_sample
import random

# TODO: If i'm on node with no neighbors, actual algorithm not work properly
def random_walk(graph:PapaGraph, start:int, lenght:int, p:float=1.0, q:float=1.0):
    '''Generate a random walk starting from `start`

    Input
    ----
    `start`: Start node
    `lenght`: Lenght of the walk
    `p`: Return paramenter
    `q`: In-Out paramenter

    Output
    ----
    `walk`: A list of nodes representing a random walk
    '''
    assert start>=0 and start<graph.nodes_number
    assert isinstance(p, float)
    assert isinstance(q, float)
    
    walk:list = [start]
    prev:int = None
    actual:int = start

    steps_distance:list = steps_from(graph=graph, start=start) 

    for step in range(lenght):
        neighbors:list[tuple] = graph.neighbors(actual)
        probability_sum:float = 0.0
        probabilities:list[float] = []

        for neighbor_index, edge_index in neighbors:
            if neighbor_index == prev:
                probabilities.append(1.0/p)
            elif steps_distance[neighbor_index] > steps_distance[actual]:
                probabilities.append(1.0/q)
            else: 
                probabilities.append(1.0)

        probability_sum:float = sum(probabilities)

        probability_remain:float = random.uniform(0,probability_sum)
        prev = actual
        for i, (neighbor_index, edge_index) in enumerate(neighbors):
            if probability_remain <= probabilities[i]:
                actual = neighbor_index
                break
            else:
                probability_remain = probability_remain - probabilities[i]
        
        walk.append(actual)

    return walk   

def random_walk_r(graph:PapaGraph, start:int, r:int, lenght:int, p:float=1.0, q:float=1.0): 
    '''Generate ``r`` random walks starting from `start`.
    
    Input
    ----
    `start`: Start node
    `lenght`: Lenght of the walk
    `r`: Quantity of random walks
    `p`: Return paramenter
    `q`: In-Out paramenter

    Output
    ----
    `walks`: A list of lists of nodes representing random walks
    '''

    walks = []
    for i in range(r):
        walks.append(random_walk(graph, start, lenght, p, q))
    return walks

if __name__ == '__main__':
    graph = handmade_sample()
    # print(random_walk(graph, 0, 5))
    print(random_walk_r(graph, 0, 5, 4))