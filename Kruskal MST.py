
"""Add edges in increasing weight, skipping those whose addition would create a cycle."""

Map = {'1-2': 853.40, '2-3': 160, '2-23': 933.9, '3-4': 170, '3-5': 158.7, '5-6': 142.8, '4-8': 256.7, '6-7': 68.7,
     '7-8': 27.2, '8-9': 142.7, '7-10': 36.8, '10-11': 27.2, '8-11': 36.8, '11-12': 126, '12-13': 208.2, '12-14': 363.6,
     '14-15': 118, '13-16': 328.2, '15-16': 150, '14-17': 100, '15-18': 100, '18-19': 100, '18-17': 118, '16-19': 115,
     '20-21': 166.4, '18-21': 152.8, '21-26': 170, '26-25': 84.2, '26-27': 130, '27-28': 170, '28-35': 115,
     '35-34': 170, '27-34': 115, '34-36': 235, '36-33': 72, '33-26': 574, '25-24': 140, '24-23': 100, '23-22': 100,
     '22-31': 371.35, '24-30': 100, '23-29': 100, '29-30': 100, '29-32': 170, '32-33': 285, '32-31': 100, '17-20': 115}


class Kruskal:
    def __init__(self, graph):
        self.graph = self.graph = {tuple(i.split('-')): j for i, j in zip(graph.keys(), graph.values())}
        self.mst = []               # list that will contain the edges of the minimum spanning tree

        # the keys of the graph(dictionary) are the edges
        edges = list(self.graph.keys())
        edges.sort(key=lambda edge: self.graph[edge])  # sort the edges by the distance between the nodes in the edge
        self.edges = edges
        self.create()
        self.grow_tree()
        self.display_results()

    def create(self):
        self.nodes = set()
        for edge in self.edges:
            self.nodes.update(edge)
        # create the union find data structure, it is a list of sets. Each set is a node in the graph
        self.ufds = [{i} for i in self.nodes]

    def find(self, node):
        """ find the position of the node in the Union-Find-Data-Structure"""
        for component in self.ufds:
            if node in component:
                return component

    def union(self, x, y):
        """Updates the Union-Find-Data-Structure by removing the individual components from it and adding a union of
        the individual components  """
        self.ufds.remove(x)
        self.ufds.remove(y)
        new_component = x | y
        self.ufds.append(new_component)
        return self.ufds

    def grow_tree(self):
        for edge in self.edges:       # iterate through the already sorted edges
            x, y = edge               # separate the edge into component nodes
            j = self.find(x)          # find the component of each node in the Union-Find-Data-Structure
            k = self.find(y)
            if j != k:                # if the nodes are in different components in the Union-Find-Data-Structure
                self.mst.append(edge)   # grow the tree by appending the edge containing the nodes to tree
                self.union(j, k)        # join the separate components of in the Union-Find-Data-Structure together
            else:
                pass  # if the edges are in the same component then add in it to the MST will create a cycle

            # when the number of edges is equivalent to the number of nodes minus one.
            if len(self.mst) == len(self.nodes) - 1:
                break               # stop the iteration because all nodes has been covered

    def display_results(self):
        total = 0
        for edge in self.mst:
            print(f"{edge} \t\t {self.graph[edge]}")
            total += self.graph[edge]
        print(f'The Total weight of the Tree is {total}')


Kruskal(Map)
