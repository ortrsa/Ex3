from DiGraph import DiGraph

graph = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
edge = {1: 2, 2: 3, 3: 4}
if __name__ == '__main__':
    p = DiGraph(graph, edge, [])

print(p.e_size())
