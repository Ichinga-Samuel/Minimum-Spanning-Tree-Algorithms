from functools import total_ordering
from pprint import pprint as pp


class Vertex:
    def __init__(self, name):
        self.name = str(name)

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"


@total_ordering
class Edge:
    def __init__(self, *, start: Vertex, end: Vertex, weight=None, direction=0):
        """A class representing an edge in a graph. If direction is 0. Then the edge is not directed.
        1 is a positive direction from start to end and -1 the reverse
        """
        self.start = start
        self.end = end
        self.weight = weight
        self.direction = direction

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __hash__(self):
        return hash(self.start) ^ hash(self.end) ^ hash(self.direction) ^ hash(self.weight)

    def __str__(self):
        return f'{self.start}<-->{self.end}: {self.weight}'

    def __repr__(self):
        return f'Edge(start={self.start}, end={self.end}, weight={self.weight}, direction={self.direction})'

    def other(self, other: Vertex):
        return self.start if other == self.end else self.end


class Graph:
    def __init__(self, data: dict = None):
        self.data = data
        self.vertices = list()
        self.edges = list()
        self.graph: dict[Vertex, dict[Vertex, Edge]] = {}

    def __len__(self):
        return len(self.vertices)

    def __contains__(self, item):
        item = Vertex(item) if not isinstance(item, Vertex) else item
        return item in self.vertices

    def __getitem__(self, item: str | Vertex) -> dict[Vertex, Edge]:
        key = Vertex(item) if not isinstance(item, Vertex) else item
        value = self.graph.get(key, None)
        if value is None:
            raise KeyError(f"Vertex {key} not found in graph")
        return value

    def __setitem__(self, vertex: Vertex, edge: Edge):
        self.graph[vertex] = self.graph.get(vertex, {}) | {edge.other(vertex): edge}
        self.vertices.append(vertex) if vertex not in self.vertices else ...
        self.edges.append(edge) if edge not in self.edges else ...

    def __iter__(self):
        return iter(self.vertices)

    @property
    def order(self):
        return len(self.vertices)

    @property
    def size(self):
        return len(self.edges)

    @property
    def weight(self):
        """
        Returns:
            float: Weight of an MST as the sum of all the edges
        """
        return sum(edge.weight for edge in self.edges)

    def build(self):
        """
        Build the graph from a dictionary with the below structure:
        {
            'v1': [('v2', 3)],
            'v2': [('v1', 3)]
        }
        """
        for vertex, neighbours in self.data.items():
            start = Vertex(vertex)
            for neighbour in neighbours:
                end = Vertex(neighbour[0])
                edge = Edge(start=start, end=end, weight=neighbour[1])
                self[start] = edge

    def build_edges(self):
        """
        Build from a dictionary of edges as shown below:
        {'v1-v2': 3}
        """
        for key, value in self.data.items():
            v1, v2 = key.split('-')
            start, end = Vertex(v1), Vertex(v2)
            edge = Edge(start=start, end=end, weight=value)
            self[start] = edge
            self[end] = edge

    def kruskal(self):
        union = UnionFind(self.vertices)
        mst = Graph()
        self.edges.sort()
        for edge in self.edges:
            find = union.union_find(edge.start, edge.end)
            if find:
                mst[edge.start] = edge
                mst[edge.end] = edge
        return mst

    def prim(self):
        mst = Graph()
        mst.vertices.append(self.vertices[0])
        while mst.order < self.order:
            edge = min([edge for vertex in mst.vertices for neighbour, edge in self[vertex].items()
                        if edge not in mst.edges and neighbour not in mst.vertices])
            mst[edge.start] = edge
            mst[edge.end] = edge
        return mst

    def show(self):
        print('Total Weight: ', self.weight)
        pp(self.graph)


class UnionFind:
    def __init__(self, vertices):
        self.data = [{vertex} for vertex in vertices]

    def union(self, set1, set2):
        self.data.remove(set1)
        self.data.remove(set2)
        self.data.append(set1 | set2)

    def find(self, vertex):
        for component in self.data:
            if vertex in component:
                return component

    def union_find(self, vertex1, vertex2):
        set1 = self.find(vertex1)
        set2 = self.find(vertex2)
        if set1 == set2:
            return False
        self.union(set1, set2)
        return True


# A graph of edges and there associated weights
graph = {'1-2': 853.40, '2-3': 160, '2-23': 933.9, '3-4': 170, '3-5': 158.7, '5-6': 142.8, '4-8': 256.7, '6-7': 68.7,
         '7-8': 27.2, '8-9': 142.7, '7-10': 36.8, '10-11': 27.2, '8-11': 36.8, '11-12': 126, '12-13': 208.2,
         '12-14': 363.6,
         '14-15': 118, '13-16': 328.2, '15-16': 150, '14-17': 100, '15-18': 100, '18-19': 100, '18-17': 118,
         '16-19': 115,
         '20-21': 166.4, '18-21': 152.8, '21-26': 170, '26-25': 84.2, '26-27': 130, '27-28': 170, '28-35': 115,
         '35-34': 170, '27-34': 115, '34-36': 235, '36-33': 72, '33-26': 574, '25-24': 140, '24-23': 100, '23-22': 100,
         '22-31': 371.35, '24-30': 100, '23-29': 100, '29-30': 100, '29-32': 170, '32-33': 285, '32-31': 100,
         '17-20': 115}

graph = Graph(data=graph)
graph.build_edges()  # use build edges
# compute mst with kruskal
mst = graph.kruskal()
# show the weight and the resulting graph
mst.show()

# using prim
mst = graph.prim()
# show the weight and the resulting graph
mst.show()

# another type of graph
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
# build with build method
graph1.build()

# solve mst with prim and kruskal
prim_mst = graph1.prim()
prim_mst.show()

kruskal_mst = graph1.kruskal()
kruskal_mst.show()
