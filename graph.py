from typing import List, Dict


class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def __repr__(self):
        return f"{self.__class__.__name__}({self.vertex1}, {self.vertex2}, {self.weight})"

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __hash__(self):
        return hash((*self.vertices, self.weight))

    def __contains__(self, item):
        return item in self.vertices

    @property
    def vertices(self):
        return self.vertex1, self.vertex2

    def difference(self, vertex1):
        return self.vertex2 if vertex1 == self.vertex1 else self.vertex1


class Graph:

    def __init__(self, data: Dict[str, float] | List[Edge], separator: str = "-"):
        """
        The edges of the graph are the keys of the dict object and the values are the weights
        The edges are two vertices separated by a single char separator like eg dash "-".
        :param data: A Dict Object
        """
        self.separator = separator
        self.graph = [Edge(*item[0].split(self.separator), item[1]) for item in data.items()] if isinstance(data, Dict) else data

    def __len__(self):
        return self.size

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.__class__(self.graph[item])
        return self.graph[item]

    def __iter__(self):
        return (edge for edge in self.graph)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.graph + other.graph

        if isinstance(other, Edge):
            return self.graph + [other]

        raise TypeError(f"{type(other)} can not be added to a graph")

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.graph.extend(other.graph)
            return self

        if isinstance(other, Edge):
            self.graph.append(other)
            return self

        raise TypeError(f"{type(other)} can not be added to a graph")

    def sort(self, key=lambda edge: edge.weight, reverse=False):
        self.graph.sort(key=key, reverse=reverse)

    def adjacency_list(self):
        adj_list = {vertex: [] for vertex in self.vertices}
        for edge in self:
            adj_list[edge.vertex1].append(edge.vertex2)
            adj_list[edge.vertex2].append(edge.vertex1)
        return adj_list

    def adjacency_list_edges(self):
        adj_list = {vertex: [] for vertex in self.vertices}
        for edge in self:
            adj_list[edge.vertex1].append(edge)
            adj_list[edge.vertex2].append(edge)
        return adj_list

    @property
    def size(self):
        return len(self.graph)

    @property
    def order(self):
        return len(self.vertices)

    @property
    def cost(self):
        return sum(edge.weight for edge in self)

    @property
    def vertices(self) -> List[str]:
        vertices = set()
        for edge in self.graph:
            vertices.update(edge.vertices)
        return list(vertices)
