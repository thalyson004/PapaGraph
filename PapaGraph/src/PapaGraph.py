
class PapaGraph:
    nodes_number:int = 0
    nodes_features:list[dict] = None

    edges_number:int = 0
    edges_features:list[dict] = None
    edges_list:list[tuple] = []

    graph_features:dict = {}

    def __init__(self):
        pass

if __name__ == '__main__':
    graph = PapaGraph()
    print(graph.nodes_number)
    print(graph.nodes_features)

    print(graph.edges_number)
    print(graph.edges_features)
    print(graph.edges_list)