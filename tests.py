"""
Unit tests for graph implementation and for PageRank algorithm.
Use with nosetests.
"""

from .graph import Graph

from nose.tools import assert_equals

def test_graph_init():
    # Test that initializing graph to a given dictionary works
    graph_dict = {
            'a': ['b'],
            'b': ['c'],
            'c': []
        }

    test_graph = Graph(graph_dict)

    assert_equals(test_graph.graph, graph_dict)


def test_graph_add_node():
    # Test that adding a node to an empty graph works
    test_graph = Graph()
    test_graph.add_node('a')

    assert_equals(test_graph.graph, {'a': []})

    test_graph.add_node('b', ['a'])
    assert_equals(test_graph.graph, {'a': [], 'b': ['a']})


def test_graph_add_edge():
    # Test adding an edge to the graph
    test_graph = Graph()
    test_graph.add_node('a')
    test_graph.add_node('b')

    assert_equals(test_graph.graph, {'a': [], 'b': []})

    test_graph.add_edge('a', 'b')

    assert_equals(test_graph.graph, {'a': ['b'], 'b': []})

