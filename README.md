# Minimum Spanning Tree Algorithms

Kruskal and Prim Minimum Spanning Tree Algorithms written in Python Object-Oriented Programming(OOP) style.
Accepts the input graph as a dictionary.

### Example
```python

# the graph as a dictionary of edges and their weight
graph = {'1-2': 853.40, '2-3': 160, '2-23': 933.9, '3-4': 170, '3-5': 158.7, '5-6': 142.8, '4-8': 256.7, '6-7': 68.7,
         '7-8': 27.2, '8-9': 142.7, '7-10': 36.8, '10-11': 27.2, '8-11': 36.8, '11-12': 126, '12-13': 208.2, '12-14': 363.6,
         '14-15': 118, '13-16': 328.2, '15-16': 150, '14-17': 100, '15-18': 100, '18-19': 100, '18-17': 118, '16-19': 115,
         '20-21': 166.4, '18-21': 152.8, '21-26': 170, '26-25': 84.2, '26-27': 130, '27-28': 170, '28-35': 115,
         '35-34': 170, '27-34': 115, '34-36': 235, '36-33': 72, '33-26': 574, '25-24': 140, '24-23': 100, '23-22': 100,
         '22-31': 371.35, '24-30': 100, '23-29': 100, '29-30': 100, '29-32': 170, '32-33': 285, '32-31': 100, '17-20': 115}

graph = Graph(graph=graph)
# use build edges because of the type of graph
graph.build_edges()
prim_mst = graph.prim()
kruskal_mst = graph.kruskal()
prim_mst.show()
kruskal_mst.show()

# Another type of input
graph1 = {
    0: [(1, 4), (7, 8), ],
    1: [(0, 4), (7, 11), (2, 8)],
    2: [(1, 8), (8, 2), (5, 4), (3, 7)],
    3: [(2, 7), (4, 9), (5, 14)],
    4: [(3, 9), (5, 10)],
    5: [(2, 4), (3, 14), (6, 2), (4, 10)],
    6: [(7, 1), (5, 2), (8, 6)],
    7: [(0, 8), (1, 11), (8, 7), (6, 1)],
    8: [(2, 2), (6, 6), (7, 7)]
}

graph1 = Graph(data=graph1)
# use another style to build the graph
graph1.build()
prim_mst = graph1.mst()
kruskal_mst = graph.kruskal()

prim_mst.show()
kruskal_mst.show()
```
