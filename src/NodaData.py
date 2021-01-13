import math
import numpy as np
import copy

Counter = 0


class NodeData:

    def __init__(self, X=None, Y=None, Z=None, Key=Counter, Info=""):
        """constructor for node data"""
        global Counter
        Counter = Counter + 1
        self.Info = Info
        self.pos = (X, Y, Z)
        self.Tag = -1
        self.Weight = math.inf
        self.id = Key

    def __lt__(self, other):
        """comparator of nodes by their weight"""
        if self.Weight < other.Weight:
            return 1
        else:
            return 0

    def __eq__(self, other):
        """returns true if the nodes have same id"""
        return self.id == other.id

    def __repr__(self):
        return str(self.id)

    def as_dict(self):
        """returns a dict that represents a node without the unnecessary variables for a json"""
        res = copy.deepcopy(self.__dict__)
        try:
            del res["Tag"]
            del res["Weight"]
            del res["Info"]
            x = self.pos[0]
            y = self.pos[1]
            z = self.pos[2]
            res["pos"] = "" + str(x) + "," + str(y) + "," + str(z)
        except:
            pass
        return res
