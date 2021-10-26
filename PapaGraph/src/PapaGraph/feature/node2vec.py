from PapaGraph.PapaGraph.PapaGraph import PapaGraph
from PapaGraph.sample.handmande import handmade_sample
from PapaGraph.walk.random_walk import probability_matrix, random_walk_r, random_walk_r_all
from gensim.models import Word2Vec
import random 
import math

def listOfList2Words(lists:list[list])->list[list[str]]:
    _ = []
    for l in lists:
        _.append('&'.join( list((str(word) for word in l)) ))
    return _ 

def node2vec(   graph: PapaGraph, d:int=3, r:int=10, 
                lenght:int=10, p:float=1.0, q:float=1.0, 
                steps:int=1000, learning_rate:float=0.0001):
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
    
    walks = random_walk_r_all(graph, r=r, lenght=lenght, p=p, q=q)


    return walks

if __name__ == '__main__':
    graph = handmade_sample()
    
    walks = node2vec(graph, lenght=5, r=3)
    _ = []
    for walk in walks:
        _.append('&'.join( list((str(w) for w in walk)) ))
    print(_)

    #model = Word2Vec(str_walks, size=128, window=5, min_count=0, sg=1, workers=2, iter=1)
