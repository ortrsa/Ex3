import numpy as np

Counter = 0


class NodeData:

    def __init__(self, X=None, Y=None, Z=None, Tag=-1, Weight=-1, Key=Counter, Info=""):
        global Counter
        Counter = Counter + 1
        self.Info = Info
        self.Pos = (X, Y, Z)
        self.Tag = Tag
        self.Weight = -1
        self.Key = Key

    def __lt__(self, other):
        if self.Weight < other.Weight:
            return 1
        else:
            return 0

    def distance(self, other) -> float:
        return np.sqrt(
            (self.pos[0] - other.pos[0]) ** 2 + (self.pos[1] - other.pos[1]) ** 2 + (self.pos[2] - other.pos[2]) ** 2)

    def __eq__(self, other):
        return self.Key == other.Key and \
               self.Tag == other.Tag and \
               self.Weight == other.Weight and \
               self.Pos == other.Pos

    def __repr__(self):
        return "Key = " + str(self.Key) + " Pos = " + str(self.Pos) + " w = " + str(self.Weight)
