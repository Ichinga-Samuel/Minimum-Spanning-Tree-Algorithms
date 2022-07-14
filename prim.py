from typing import Dict
from random import choice
from pprint import pprint
from graph import Graph


class Prim:

    def __init__(self, data: Dict):
        self.graph = Graph(data)
        self.mst = Graph({})
        self.grow_mst()
        self.show()

    def grow_mst(self):
        vertices = self.graph.vertices
        adjacency = self.graph.adjacency_list_edges()
        start_vertex = choice(vertices)
        edges = adjacency[start_vertex]
        visited = {start_vertex}
        while len(self.mst) != len(vertices)-1:
            edges.sort()
            edge = edges[0]
            if (edge.vertex1 in visited) and (edge.vertex2 in visited):
                edges.remove(edge)
                continue

            self.mst += edge
            visited.update(edge.vertices)
            new_edges = {edge for edge in adjacency[edge.vertex1] + adjacency[edge.vertex2]}
            edges.extend(new_edges)

    def show(self):
        tree = {'-'.join(edge.vertices): edge.weight for edge in self.mst}
        pprint(tree, indent=2)
        print("Total Weight:", self.mst.cost)


graph = {'1-2': 853.40, '2-3': 160, '2-23': 933.9, '3-4': 170, '3-5': 158.7, '5-6': 142.8, '4-8': 256.7, '6-7': 68.7,
         '7-8': 27.2, '8-9': 142.7, '7-10': 36.8, '10-11': 27.2, '8-11': 36.8, '11-12': 126, '12-13': 208.2, '12-14': 363.6,
         '14-15': 118, '13-16': 328.2, '15-16': 150, '14-17': 100, '15-18': 100, '18-19': 100, '18-17': 118, '16-19': 115,
         '20-21': 166.4, '18-21': 152.8, '21-26': 170, '26-25': 84.2, '26-27': 130, '27-28': 170, '28-35': 115,
         '35-34': 170, '27-34': 115, '34-36': 235, '36-33': 72, '33-26': 574, '25-24': 140, '24-23': 100, '23-22': 100,
         '22-31': 371.35, '24-30': 100, '23-29': 100, '29-30': 100, '29-32': 170, '32-33': 285, '32-31': 100, '17-20': 115}

mst = Prim(graph)
