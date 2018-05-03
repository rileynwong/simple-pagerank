from graph import Node, Graph
from pagerank import pagerank

a = Node()
b = Node()
c = Node()
d = Node()

g = Graph()

g.add_node('a', a)
g.add_node('b', b)
g.add_node('c', c)
g.add_node('d', d)

g.add_edge('b', 'a')
g.add_edge('c', 'a')
g.add_edge('d', 'a')

ranks = pagerank(g, 1)

for node, value in ranks.items():
    print(node.name, value)
