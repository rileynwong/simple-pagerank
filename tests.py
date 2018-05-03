"""
Unit tests for graph implementation.
Use with nosetests.
"""

from .graph import Graph
from .graph import Node

from nose.tools import assert_equals

### Test graph implementation
def test_graph_init():
    # Test that initializing graph to a given dictionary works
    node_dict = {
            'a': Node(),
            'b': Node(),
            'c': Node()
        }

    test_graph = Graph(node_dict)

    assert_equals(test_graph.nodes, node_dict)


def test_graph_add_node():
    # Test that adding a node to an empty graph works
    test_graph = Graph()
    node_a = Node()

    test_graph.add_node('a', node_a)

    assert_equals(test_graph.nodes['a'].inbound, [])
    assert_equals(test_graph.nodes['a'].outbound, [])

    node_b = Node(inbound=[], outbound=[node_a])
    test_graph.add_node('b', node_b)

    assert_equals(test_graph.nodes['b'].inbound, [])
    assert_equals(test_graph.nodes['b'].outbound, [node_a])

    assert len(test_graph.nodes) == 2


def test_graph_add_edge():
    # Test adding an edge to the graph
    test_graph = Graph()
    node_a = Node()
    node_b = Node()

    test_graph.add_node('a', node_a)
    test_graph.add_node('b', node_b)

    assert_equals(test_graph.nodes, {'a': node_a, 'b': node_b})

    test_graph.add_edge('a', 'b')

    assert_equals(node_a.outbound, [node_b])
    assert_equals(node_b.inbound, [node_a])

