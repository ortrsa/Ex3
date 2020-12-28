from functools import cmp_to_key
import numpy

class Edge:

    def __init__(self, src, dest, whight, info, tag):
        self.tag = tag
        self.info = info
        self.whight = whight
        self.dest = dest
        self.src = src

    def __eq__(self, other):
        return self.src == other.src and \
               self.dest == other.destand and \
               self.weight == other.weight
