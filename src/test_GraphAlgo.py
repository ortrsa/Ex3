from unittest import TestCase

from GraphAlgo import GraphAlgo
from network import Network


class TestGraphAlgo(TestCase):
    def setUp(self) -> None:
        global Galgo
        global NG
        Galgo = GraphAlgo()
        NG = Network('../data/A5')
        Galgo.load_from_json('../data/A5')

    def test_get_graph(self):
        (dis,test_list) = Galgo.shortest_path(0, 5)
        self.assertEqual(1, 1)
        self.assertEqual(0,test_list[0].id,"key of this node should be 0")
        self.assertEqual(2,test_list[1].id,"key of this node should be 2")
        self.assertEqual(3, test_list[2].id, "key of this node should be 3")
        self.assertEqual(13, test_list[3].id, "key of this node should be 13")
        self.assertEqual(5, test_list[4].id, "key of this node should be 5")
        self.assertEqual(5,test_list.__len__(),"there should be 5 nodes in that path")
        self.assertEqual(4.685698594072881,dis,"shortest path distance should be 4.685698594072881")
        Galgo.G.remove_node(13)
        (dis1,test_list1)= Galgo.shortest_path(0,5)
        print(dis1)


    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        self.fail()

    def test_connected_component(self):
        self.fail()

    def test_connected_components(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()

    def test_reset_w(self):
        self.fail()
