from unittest import TestCase
from GraphAlgo import GraphAlgo
from network import Network
from DiGraph import DiGraph
import networkx as nx

filename = '../data/A5'
Galgo = GraphAlgo()
Galgo.load_from_json(filename)
NG = Network(filename)


class TestDiGraph(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_v_size(self):
        NG.G.remove_node(13)
        NG.G.remove_node(12)
        NG.G.remove_node(11)
        NG.G.remove_node(10)

        self.assertEqual(Galgo.G.v_size(), nx.number_of_nodes(NG.G))

    def test_e_size(self):
        self.assertEqual(Galgo.G.v_size(), nx.number_of_nodes(NG.G))

    def test_get_all_v(self):
        self.fail()

    def test_all_in_edges_of_node(self):
        self.fail()

    def test_all_out_edges_of_node(self):
        self.fail()

    def test_add_edge(self):
        self.fail()

    def test_add_node(self):
        self.fail()

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()
