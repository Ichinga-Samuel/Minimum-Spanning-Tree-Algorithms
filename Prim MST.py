
""" The input to the python class that solve this minimum spanning tree problem is a dictionary(mapping) containing the
	edges and the distance between them as key-value pairs e.g the distance between node 1 to node 2 is 853.4 on the 
	network it will be represented as edge '1-2': 853.4. The nodes can be represented as anything eg. node 1 can be
	written as 'Gate' and node 2 can be written as 'Hostel'. That edge will now be written as 'Gate-Hostel': 853.4.
	To pass in a different network to the class just create a dictionary like the one below with edges and distances as
	key: value pairs, assign the dictionary to a variable and then pass the variable into the class.
"""
Map = {'1-2': 853.40, '2-3': 160, '2-23': 933.9, '3-4': 170, '3-5': 158.7, '5-6': 142.8, '4-8': 256.7, '6-7': 68.7,
	'7-8': 27.2, '8-9': 142.7, '7-10': 36.8, '10-11': 27.2, '8-11': 36.8, '11-12': 126, '12-13': 208.2, '12-14': 363.6,
	'14-15': 118, '13-16': 328.2, '15-16': 150, '14-17': 100, '15-18': 100, '18-19': 100, '18-17': 118, '16-19': 115,
	'20-21': 166.4, '18-21': 152.8, '21-26': 170, '26-25': 84.2, '26-27': 130, '27-28': 170, '28-35': 115,
	'35-34': 170, '27-34': 115, '34-36': 235, '36-33': 72, '33-26': 574, '25-24': 140, '24-23': 100, '23-22': 100,
	'22-31': 371.35, '24-30': 100, '23-29': 100, '29-30': 100, '29-32': 170, '32-33': 285, '32-31': 100, '17-20': 115}


class PrimMST:

	def __init__(self, graph, node=''):

		"""Initialize the class with a graph containing the edges and optionally
		the node you wish to start with. If no node is set during initialization,
		a node is randomly chosen"""

		self.graph = {tuple(i.split('-')): j for i, j in zip(graph.keys(), graph.values())}

		# create the edges from the keys of the input graph
		self.edges = list(self.graph.keys())
		self.edges.sort(key=lambda edge: self.graph[edge])
		self.nodes = self._nodes()  # a set containing the nodes of the graph

		# This randomly chooses a node if none is specified
		self.n = node or self.nodes[0]
		
		# Adds the first node to the set containing the nodes already covered by the MST
		self.mnodes = {self.n}

		self.priority_queue = []  # the priority queue contain all the edges connected to nodes in the MST as it grows
		
		# A List That Will Contain the MST i.e the Edges That Make up the solution
		self.MST = []

		self.grow_mst()
	
	def _nodes(self):
		"""A method to return the nodes in the Tree"""
		nodes = set()
		for edge in self.edges:
			nodes.update(edge)
		return list(nodes)
	
	def initialize_priority_queue(self):
		"""This method creates the initial priority queue from the starting node"""
		for edge in self.edges:
			if self.n in edge:
				self.priority_queue.append(edge)
				
	def remove_from_queue(self):
		"""This method removes from the priority queue those edges whose nodes are already connected by other edges"""

		# Make a copy of the priority queue to iterate through while altering the priority queue itself
		pq = self.priority_queue[:]
		for edge in pq:
			# checks to see if both nodes of that edge is in the list of connected nodes
			if edge[0] in self.mnodes and edge[1] in self.mnodes:
				# Remove the edge from the priority queue and the copy of the graph that we are choosing from
				self.priority_queue.remove(edge)
				self.edges.remove(edge)
	
	def grow_priority_queue(self):
		# update the priority queue by to adding the edges connected to the last set of nodes in the MST
		last_edge = self.MST[-1]
		for edge in self.edges:
			if edge[0] in last_edge or edge[1] in last_edge:
				self.priority_queue.append(edge)
				continue	
		# removes duplicates from the priority queue
		self.priority_queue = list(set(self.priority_queue))
			
	def Mst(self):
		"""This method adds to the MST using the first edge in the priority queue and extends the
		priority queue using the last edge in the MST"""
		
		# Sort the priority queue to get the edge with the smallest weight currently in the queue
		self.priority_queue.sort(key=lambda edge: self.graph[edge])
		
		# Add the smallest edge currently in the queue to the MST
		self.MST.append(self.priority_queue[0])
		
		# obtain the last edge in the Self.MST split it into constituent nodes and update the nodes set with it
		self.mnodes.update(self.MST[-1])

	def grow_mst(self):
		"""This method grows the MST using the extends and remove from queue methods"""
		self.initialize_priority_queue()
		for i in range(len(self.graph)):
			self.remove_from_queue()
			self.Mst()
			self.grow_priority_queue()
			if len(self.MST) == len(self.nodes)-1:
				break

		self.display()

	def display(self):
		for edge in self.MST:
			print(f'{edge} \t {self.graph[edge]}')
		
		Total = sum(self.graph[i] for i in self.MST)
		print(f'The Total Weight is {Total}')
					

PrimMST(Map)
