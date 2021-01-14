from src.GraphInterface import GraphInterface
from NodaData import NodeData
import random


class DiGraph(GraphInterface):
    def __init__(self):
        """constructor for a graph"""
        self.graph = {}
        self.oute = {}
        self.ine = {}
        self.MC = 0
        self.edgeSize = 0

    def v_size(self) -> int:
        """returns the number of nodes that are in the graph by the size of the dict that we saved them in"""
        return len(self.graph)

    def e_size(self) -> int:
        """returns the nukber of edges that are in the graph"""
        return self.edgeSize

    def get_all_v(self) -> dict:
        """returns a dictionary of the nodes that are in the graph by key:node , value :NodeData"""
        return self.graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        """returns a dict of all the nodes that has edges to the wanted node by id1 and the value is the weight of
        the edge """
        if id1 not in self.ine.keys():
            tmp = {}
            return tmp
        return self.ine[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        """returns a dict of all the nodes that the wanted node by id1 has edges to and the value is the weight of
                the edge """
        if id1 not in self.oute.keys():
            tmp = {}
            return tmp
        return self.oute[id1]

    def get_mc(self) -> int:
        """returns the number of times we affected on the graph with function"""
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """connects to nodes by adding them to the hashmaps *oute and *ine oute represents the edges that go from
         a node to other node and ine represents that edges that go into a node.
         of course we first check if the nodes are in the graph and if the weight is not negative. """
        if id1 == id2:
            return False
        if id1 not in self.graph.keys() or id2 not in self.graph.keys():
            return False
        if weight < 0:
            return False
        if id2 not in self.oute[id1].keys():
            self.edgeSize += 1
        else:
            return False
        self.MC += 1
        self.oute[id1][id2] = weight
        self.ine[id2][id1] = weight
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """adds a node to the graph by creating a new node with the information we get at the head of
        the function and adding it to the graph dict by key: node id and value: the node we created.
        first of all we check if this node isnt exists at the graph already."""
        if self.graph is not None:
            if node_id in self.graph.keys():
                return False
        if pos is None:
            X = random.uniform(0.0, 10.0)
            Y = random.uniform(0.0, 10.0)
            Z = 0
        else:
            X = pos[0]
            Y = pos[1]
            Z = pos[2]

        node = NodeData(X, Y, Z, Key=node_id)
        self.graph[node_id] = node
        self.oute[node_id] = {}
        self.ine[node_id] = {}
        self.MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """removes a node from the graph by deleting him from the graph dictionary
        then going to all the nodes that have an edge from them to the wanted node and delet this edge
        then delet all the edges that go out from him and finally remove him from the oute and ine dict
        if there isnt such a node in the graph returns false otherwise true;"""
        if node_id not in self.graph.keys():
            return False

        a = set(self.all_in_edges_of_node(node_id).keys())
        for i in a:
            if self.remove_edge(i, node_id):
                self.MC -= 1
        b = set(self.all_out_edges_of_node(node_id).keys())
        for i in b:
            if self.remove_edge(node_id, i):
                self.MC -= 1
        del self.oute[node_id]
        del self.ine[node_id]
        del self.graph[node_id]
        self.MC += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """delets an edge between to nodes only if it exists by delete from oute dict at place src
        the dest and from ine dict at place dest delet the src """
        if node_id1 not in self.graph.keys() or node_id2 not in self.graph.keys():
            return False
        if node_id2 not in self.oute[node_id1].keys():
            return False
        del self.oute[node_id1][node_id2]
        del self.ine[node_id2][node_id1]
        self.edgeSize -= 1
        self.MC += 1
        return True

    def __str__(self) -> str:
        """prints the nodes number and edges number"""
        return "Graph: |V|=" + str(len(self.graph)) + " , |E|=" + str(self.edgeSize)

    def as_dict(self):
        return self.__dict__

    def __eq__(self, other):
        temp = self.v_size()
        temp2 = self.edgeSize
        temp3 = other.edgeSize
        if temp3 != temp2:
            return False
        for i in self.graph.keys():
            if not self.graph.__contains__(i):
                return False
            for j in self.all_out_edges_of_node(i):
                if self.oute[i][j] != other.oute[i][j]:
                    return False
            for k in self.all_in_edges_of_node(i):
                if self.ine[i][k] != other.ine[i][k]:
                    return False
        return self.v_size() == other.v_size()
