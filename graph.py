"""
Simple Python implementation of a directed graph.
"""
class Node(object):
    def __init__(self, inbound=None, outbound=None):
        self.name = ''

        if inbound:
            self.inbound = inbound
        else:
            self.inbound = []

        if outbound:
            self.outbound = outbound
        else:
            self.outbound = []

    def add_outbound_edge(self, node):
        # Add directed edge from this node to another node
        self.outbound.append(node)
        node.inbound.append(self)

    def add_inbound_edge(self, node):
        # Add directed edge from another node to this node
        self.inbound.append(node)
        node.outbound.append(self)


class Graph(object):
    # Note: Does not account for error-checking
    """ A dictionary of Nodes. Key is node name, value is node object. """

    def __init__(self, nodes=None):
        if nodes:
            self.nodes = nodes
        else:
            self.nodes = {}

    def add_node(self, node_name, node):
        # Add node to graph
        node.name = node_name
        self.nodes[node_name] = node

    def add_edge(self, start_node, end_node):
        # Add edge from start node to end node
        start = self.nodes[start_node]
        end = self.nodes[end_node]

        start.add_outbound_edge(end)

    def get_neighbors(self, node_name):
        # Return outbound neighbors for a given node
        node = self.nodes[node_name]
        neighbors = node.outbound
        return neighbors

    def remove_node(self, node_name):
        # Remove node and its outbound edges from the graph
        if node_name in self.graph:
            del self.nodes[node_name]

    """ # Running out of time ...
    def remove_edge(self, start_node, end_node):
        start = self.nodes[start_node]
        end = self.nodes[end_node]

        # Remove directed edge from start node to end node
        self.nodes[start_node].remove(end_node)
    """

    def get_nodes(self):
        # Return a list of nodes
        nodes = list(self.nodes.values())
        return nodes



