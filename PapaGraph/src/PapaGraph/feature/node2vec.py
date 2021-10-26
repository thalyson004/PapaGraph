from PapaGraph.PapaGraph.PapaGraph import PapaGraph
from PapaGraph.sample.handmande import handmade_sample
from PapaGraph.walk.random_walk import probability_matrix, random_walk_r, random_walk_r_all
from gensim.models import Word2Vec
import random 
import math

def listOfListAny2listOfListStr(lists:list[list])->list[list[str]]:
    return [[str(w) for w in word] for word in lists]

def node2vec(   graph: PapaGraph, d:int=3, r:int=10, 
                lenght:int=10, p:float=1.0, q:float=1.0, 
                steps:int=5, learning_rate:float=0.025):
    ''' Return a matrix that mapping each node in a `d` dimensional space.

    Input
    ----
    `graph`: A PapaGraph
    `d`: Number of features
    `r`: Number of random walks
    `lenght`: Lenght of each random walk
    `p`: Return parameter
    `q`: In-Out paramenter
    `steps`: Number of steps using Gradiente Descent
    Output
    ----
    `features`: Mapping matrix

    '''
    
    walks = random_walk_r_all(graph, r=r, lenght=lenght, p=p, q=q)
    words = listOfListAny2listOfListStr(walks)
    model = Word2Vec(   words, 
                        window=5, min_count=1, sg=1, 
                        workers=2, alpha=learning_rate,
                        epochs=steps)
    '''
        This model give features for each node
        To get features by node, use: model.wv[str(0)]
    '''
    
    

    return words

if __name__ == '__main__':
    graph = handmade_sample()
    
    words = node2vec(graph, lenght=5, r=3)

