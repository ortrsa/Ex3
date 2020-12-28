from DiGraph import DiGraph
from Edge import Edge
from NodaData import NodeData

if __name__ == '__main__':
    graph = DiGraph()
    graph.add_node(1, (1, 2, 3))
    graph.add_node(2, (2, 3, 4))
    graph.add_node(3, (4, 5, 6))
    graph.add_node(4, (5, 6, 7))

    print(graph.add_edge(1, 2, 3))
    print(graph.add_edge(3, 2, 4))
    print(graph.add_edge(1, 1, 6))

    print(graph.get_mc())
