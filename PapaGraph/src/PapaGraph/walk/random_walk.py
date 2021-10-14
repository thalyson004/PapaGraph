from PapaGraph.PapaGraph.PapaGraph import PapaGraph

def random_walk(graph:PapaGraph, start:int, lenght:int, p:float=0.5, q:float=None):
    '''Generate a random_walk starting.
    `start`: Start node
    `lenght`: Lenght of the walk
    `p`: Return paramenter
    `q`: Walk away paramenter
    '''
    assert start>=0 and start<graph.nodes_number
    assert p!=None and p>=0.0 and p<=1.0

    if q==None:
        q = 1.0-p
    else:
        assert p+q==1.0
    
    walk:list = [start]

    return walk    

if __name__ == '__main__':
    graph = PapaGraph()
    graph.add_nodes(quantity=8)
    graph.add_edge(0,1, bidirectional=True)
    graph.add_edge(0,2, bidirectional=True)
    graph.add_edge(0,3, bidirectional=True)
    graph.add_edge(1,2, bidirectional=True)
    graph.add_edge(1,7, bidirectional=True)
    graph.add_edge(2,3, bidirectional=True)
    graph.add_edge(3,4, bidirectional=True)
    graph.add_edge(4,7, bidirectional=True)
    graph.add_edge(4,5, bidirectional=True)
    graph.add_edge(4,6, bidirectional=True)
    graph.add_edge(5,6, bidirectional=True)
    
    print(random_walk(graph, 0, 3))