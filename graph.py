"""
Simple Python implementation of a directed grpah.
"""

class Graph(object):

    def __init__(self, init_dict=None):
        """
        Initialize graph dictionary. Keys are nodes, values are a list of nodes,
        representing the outbound neighbors for that given node.
        """
        if init_dict:
            self.graph = init_dict
        else:
            self.graph = {}

    def add_node(self, node_name, neighbors=None):
        # Neighbors based on outbound edges, not inbound
        if neighbors:
            self.graph[node_name] = neighbors
        else:
            self.graph[node_name] = []

    def add_edge(self, start_node, end_node):
        # Add a directed edge from the start node to the end node
        self.graph[start_node].append(end_node)

    def get_neighbors(self, node_name):
        # Return outbound neighbors for a given node
        neighbors = self.graph[node_name]
        return neighbors

    def remove_node(self, node_name):
        # Remove node and its outbound edges from the graph
        if node_name in self.graph:
            del self.graph[node_name]

    def remove_edge(self, start_node, end_node):
        # Remove directed edge from start node to end node
        self.graph[start_node].remove(end_node)





