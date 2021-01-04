import numpy as np
import copy
Counter = 0


class NodeData:

    def __init__(self, X=None, Y=None, Z=None, Tag=-1, Key=Counter, Info=""):
        global Counter
        Counter = Counter + 1
        self.Info = Info
        self.pos = (X, Y, Z)
        self.Tag = Tag
        self.Weight = -1
        self.id = Key

    def __lt__(self, other):
        if self.Weight < other.Weight:
            return 1
        else:
            return 0

    def distance(self, other) -> float:
        return np.sqrt(
            (self.pos[0] - other.pos[0]) ** 2 + (self.pos[1] - other.pos[1]) ** 2 + (self.pos[2] - other.pos[2]) ** 2)

    def __eq__(self, other):
        return self.id == other.id and \
               self.Tag == other.Tag and \
               self.Weight == other.Weight and \
               self.pos == other.pos

    # def __repr__(self):
    #     return " \"pos\":" + "\"" + str(self.pos[0]) + "," + str(self.pos[1]) + "," + \
    #            str(0) + "\"," + "\"id\":" + str(self.id)

    def __repr__(self):
        return str(self.id)

    def as_dict(self):
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
