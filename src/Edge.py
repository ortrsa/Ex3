from functools import cmp_to_key
import numpy


class Edge:

    def __init__(self, src, dest, weight, info="", tag=-1):
        self.tag = tag
        self.info = info
        self.w = weight
        self.dest = dest
        self.src = src

    def __eq__(self, other):
        return self.src == other.src and \
               self.dest == other.destand and \
               self.w == other.w

    def __repr__(self):
        return " src= " + str(self.src) + " dest= " + str(self.dest) + " weight= " + str(self.w)

    def as_dict(self):
        res = self.__dict__
        try:
            del res["tag"]
            del res["info"]
        except:
            print("not found")
        return res
