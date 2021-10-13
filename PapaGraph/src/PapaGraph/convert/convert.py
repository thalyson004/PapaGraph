
from PapaGraph.PapaGraph.PapaGraph import PapaGraph


def convert_from_ogb(ogb_graph:dict):
    try:
        nodes_number = ogb_graph['num_nodes']
        nodes_features = ogb_graph['node_feat']

        edges = ogb_graph['edge_index']
        edges_features = ogb_graph['edge_feat']
    except:
        print("The input is not a OGB Raw Graph")
        return None

    ans = PapaGraph()
    ans.nodes_number = nodes_number
    ans.nodes_features = nodes_features

    ans.edges_number = len(edges[0])
    for i in range(ans.edges_number):
        ans.edges_list.append( (edges[0][i], edges[1][i]) )
    
    ans.edges_features = edges_features 

    return ans

if __name__ == '__main__':
    print("Test")