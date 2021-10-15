from PapaGraph.PapaGraph.PapaGraph import PapaGraph
from PapaGraph.sample.handmande import handmade_sample
from PapaGraph.walk.random_walk import probability_matrix, random_walk_r
import random 

def node2vec(   graph: PapaGraph, d:int=3, r:int=10, 
                lenght:int=10, p:float=1.0, q:float=1.0, steps:int=1000):
    ''' Return a matrix that mapping each node in a `d` dimensional space.

    Input
    ----
    `graph`: A PapaGraph
    `d`: Number of features
    `r`: Number of random walks
    `lenght`: Lenght of each random walk
    `p`: Return parameter
    `q`: In-Out paramenter
    `steps`: Number of steps on Stochastic Gradiente Descent
    Output
    ----
    `features`: Mapping matrix

    '''
    
    probs = probability_matrix(graph, r, lenght, p, q)
    features = [[ random.uniform(0,1) for i in range(d) ] for j in range(graph.nodes_number)]

    def similarity_original(u:int, v:int):
        return probs[u][v]*probs[v][u]

    # for u in range(graph.nodes_number):
    #     for v in range(graph.nodes_number):
    #         print(u, v,':', similarity_original(u, v))

    def similarity_embedding(u:int, v:int):
        return sum( [features[u][i]*features[v][i] for i in range(d) ] )
    
    # for u in range(graph.nodes_number):
    #     for v in range(graph.nodes_number):
    #         print(u, v,':', similarity_embedding(u, v))

    # TODO: Optimaze the features using Stochastic Gradient Descent 
    #       (page 35: http://web.stanford.edu/class/cs224w/slides/03-nodeemb.pdf)

    


    return features

if __name__ == '__main__':
    graph = handmade_sample()
    
    features = node2vec(graph, lenght=5, r=1000)

    print("Features:")
    for feature in features:
        print( [round(f, 2) for f in feature] )

