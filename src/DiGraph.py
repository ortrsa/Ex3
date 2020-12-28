from src.GraphInterface import GraphInterface
from Edge import Edge
from NodaData import NodeData

graph: dict = {}
edges: dict = {}
parents: dict = {}


class DiGraph(GraphInterface):

    def __init__(self):
        global graph
        global edges
        global parents
        self.Graph = graph
        self.Edges = edges
        self.Parents = parents
        self.MC = 0
        self.EdgeSize = 0

    def v_size(self) -> int:
        return len(self.Graph)

    def e_size(self) -> int:
        return len(self.Edges)

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
        global graph
        if graph is not None:
            if node_id in dict(graph).keys():
                return False
        node = NodeData(X=pos[0], Y=pos[1], Z=pos[2], Key=node_id)
        graph[node_id] = node
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        raise NotImplementedError

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        raise NotImplementedError
