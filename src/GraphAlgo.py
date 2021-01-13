import math
from typing import List
import GraphInterface
import matplotlib.pyplot as plt
from src.DiGraph import DiGraph
import json
import queue
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        if graph is None:
            graph = DiGraph()
        self.G = graph

    def get_graph(self) -> GraphInterface:
        return self.G

    def load_from_json(self, file_name: str) -> bool:
        """create a graph using a saved text file by using the key words "Nodes" and "Edges"
        then split the string by , to get the X Y Z and creating a new node and adding it to the graph
         connects the nodes by Edges and w for weight src and dest"""
        self.G = DiGraph()
        try:
            with open(file_name, "r") as file:
                x = json.load(file)
                for node in x["Nodes"]:
                    if node.__contains__("pos"):
                        new_pos = [float(i) for i in node["pos"].split(",", maxsplit=2)]
                        self.G.add_node(node["id"], (new_pos[0], new_pos[1], new_pos[2]))
                    else:
                        self.G.add_node(node["id"])
                if x.__contains__("Edges"):
                    for edge in x["Edges"]:
                        self.G.add_edge(edge["src"], edge["dest"], edge["w"])

                return True
        except IOError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        """save a graph to a text file and saving his Nodes and Edges
        for the nodes well save the pos and their key
        for the edges well save the src dest and edge weight"""
        graph_dict = {}
        edge_list = []

        for i in self.G.oute.keys():
            for j in self.G.oute[i].keys():
                edge_map = {'src': i, 'w': self.G.oute[i][j], 'dest': j}
                edge_list.append(edge_map)

        try:
            with open(file_name, "w") as file:
                graph_dict["Edges"] = edge_list
                graph_dict["Nodes"] = [i for i in self.G.graph.values()]
                json.dump(graph_dict, default=lambda m: m.as_dict(), fp=file)
                return True
        except IOError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """returns a list of nodes that represents the shortest path between tow nodes and the distance as well
        using Dijkstra algorithm is an algorithm to fined the shortest path between nodes(by weight).
        this method find the shortest distance by weight from src node to all the node in the graph.
        this method based on 4 data structure path(list) , unused(PriorityQueue), used(list)
        and nodePar(dict).
        first add the src node to unused PriorityQueue and set is weight to 0,
        continue while unused is not empty,
        iterate throw all it's neighbors and every node that isnt with inf weight
        if the node weight is bigger then his father weight + the edge weight or node weight is inf
        replace the node weight with his father + the edge between the node and his father.
        (skip this step for the father node).
        add to unused PriorityQueue  , same for all neighbors.
        after that pull the next node from unused, because of the PriorityQueue every next node on the list
        will be with the lightest weight.
        after iterate throw all the graph all the nodes will be in the nodeDis Hashmap and contain in the value
        their min weight from src node.
        also the nodePar will contain every node and his father when called from shortestPath method.
        now that nodePar is full we can go from the dest node by pointer back until well get to the
        src node while we adding the nodes the pointer points on to a list which will be the shortest path list
        then we return this list(nodes we need to go for the shortest path) and the weight of the dest(the distance of that path)"""
        if id1 not in self.G.get_all_v() or id2 not in self.G.get_all_v():
            tmp = (math.inf, [])
            return tmp
        used = []
        unused = queue.PriorityQueue()
        nodePar = {}
        path = []
        self.G.graph.get(id1).Weight = 0.0
        unused.put(self.G.graph.get(id1))

        while not unused.empty():

            t = unused.get()
            if t.id == id2:
                break
            if t.id in used:
                continue
            used.append(t.id)
            for Nei in self.G.all_out_edges_of_node(t.id):

                tempNeiDis = self.G.graph.get(Nei).Weight  # nodeDis.get(Nei)
                tDis = self.G.graph.get(t.id).Weight
                EdgeDis = self.G.oute.get(t.id).get(Nei)

                if tempNeiDis > (tDis + EdgeDis):
                    self.G.graph.get(Nei).Weight = tDis + EdgeDis
                    unused.put(self.G.graph.get(Nei))
                    nodePar[Nei] = t

        if self.G.graph.get(id2).Weight == math.inf:
            self.reset_w()
            return math.inf, path

        pointernode = self.G.graph.get(id2)
        path.append(pointernode.id)
        while pointernode.id is not id1:
            pointernode = nodePar.get(pointernode.id)
            path.append(pointernode.id)
        path.reverse()
        res = self.G.graph.get(id2).Weight
        self.reset_w()
        return res, path

    def connected_component(self, id1: int) -> list:
        """returns the Strongly Connected Component(SCC) that node id1 is a part of by
        creating to sets the first one will be filled with the nodes ids that he can get to
        the second one will be filled with the nodes that can get to him then well return the
        intersection of those two lists"""
        if id1 not in self.G.get_all_v():
            return []
        connected1 = set()
        connected_to = []
        connected_from = []

        connected1.add(id1)

        while len(connected1) > 0:
            for node in self.G.all_out_edges_of_node(connected1.pop()):

                if self.G.graph.get(node).Weight == math.inf:
                    self.G.graph.get(node).Weight = 0
                    connected1.add(node)
                    connected_to.append(node)

        connected1.add(id1)

        while len(connected1) > 0:
            for node in self.G.all_in_edges_of_node(connected1.pop()):
                if self.G.graph.get(node).Tag == -1:
                    self.G.graph.get(node).Tag = 0
                    connected1.add(node)
                    connected_from.append(node)

        res = list(set(connected_from).intersection(connected_to))
        for node in self.G.get_all_v().values():
            node.Weight = math.inf
            node.Tag = -1
        if len(res) == 0:
            res.append(id1)
        return res

    def connected_components(self) -> List[list]:
        """returns all the Strongly Connected Component(SCC) in the graph.
        returns by creating a set of all the nodes keys and every time send the first
        node on this list to connected_component(node id) and save that list in a list of lists
        then removing all the nodes that are in that list from the sets of all nodes and sends the next one
        untill the set of all nodes is empty and we have list of lists of the strongly connected component in the graph."""
        all_nodes = set(self.G.get_all_v().keys())
        res = []
        if len(all_nodes) == 0:
            return res
        while len(all_nodes) > 0:
            list1 = self.connected_component(all_nodes.pop())
            res.append(list1)

            all_nodes = all_nodes - (set(list1))
        return res

    def plot_graph(self) -> None:
        """this function draws the graph by using mat_plot_lib
        we add every node by his pos and every edge by it src and dest(we draw a line between them)"""
        x = [i.pos[0] for i in self.G.get_all_v().values()]
        y = [i.pos[1] for i in self.G.get_all_v().values()]
        plt.plot(x, y, "o")
        for i in self.G.get_all_v().values():
            for j in self.G.all_out_edges_of_node(i.id):
                x1 = i.pos[0]
                y1 = i.pos[1]
                x2 = self.G.graph[j].pos[0]
                y2 = self.G.graph[j].pos[1]
                plt.annotate("", xy=(x1, y1), xytext=(x2, y2), arrowprops=dict(arrowstyle="->"))

        plt.show()

    def reset_w(self):
        """resets all the nodes weight to inf"""
        for node in self.G.get_all_v().values():
            node.Weight = math.inf
