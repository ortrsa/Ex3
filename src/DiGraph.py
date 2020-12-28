from src.GraphInterface import GraphInterface
from Edge import Edge
from NodaData import NodeData

graph: dict = {}
edges: dict = {}
parents: dict = {}
edgeSize: int = 0
MC: int = 0


class DiGraph(GraphInterface):

    def __init__(self):
        global graph
        global edges
        global parents
        global edgeSize
        global MC
        self.Graph = graph
        self.Edges = edges
        self.Parents = parents

    def v_size(self) -> int:
        return len(self.Graph)

    def e_size(self) -> int:
        return edgeSize

    def get_all_v(self) -> dict:
        return self.Graph.values()

    def all_in_edges_of_node(self, id1: int) -> dict:
        dict1 = None
        itr = iter(dict(self.par[id1]).keys())
        while True:
            try:
                temp = next(itr)
                dict1[temp] = NodeData(self.Graph.keys(temp)).Weight

            except StopIteration:
                break

        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
         """
        return dict1

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
        weight)
        """

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        raise NotImplementedError

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        global MC
        global edgeSize
        global edges

        if id1 not in graph.keys() or id2 not in graph.keys():
            return False
        if weight < 0:
            raise ValueError
        if id2 not in dict(edges[id1]).keys():
            edgeSize += 1
        elif weight == edges[id1][id2].weight:
            return False
        MC += 1
        edge = Edge(id1, id2, weight)
        edges[id1][id2] = edge
        parents[id2][id1] = edge
        return True
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        raise NotImplementedError

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if graph is not None:
            if node_id in dict(graph).keys():
                return False
        node = NodeData(X=pos[0], Y=pos[1], Z=pos[2], Key=node_id)
        graph[node_id] = node
        edges[node_id] = {}
        parents[node_id] = {}
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in graph.keys():
            return False
        del graph[node_id]
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 or node_id2 not in graph.keys():
            return False
        if node_id2 not in dict(edges[node_id1]).keys():
            return False
        del edges[node_id1][node_id2]
        del parents[node_id1][node_id1]
        edgeSize += 1
        MC += 1
        return True

    def __str__(self) -> str:

        return str(graph.values())
