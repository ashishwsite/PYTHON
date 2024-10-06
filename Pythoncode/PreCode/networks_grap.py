# NETWORKS IS WAY OF REPRESENT gRAP IN EASY WAY
import networkx as nx
import matplotlib.pyplot as plt
# initilising a grap witn empty node 
g=nx.Graph()
g.add_node(2)
g.add_node(5)
g.add_edge(2,5)
g.add_edge(9,5)
g.add_node(1)
g.add_nodes_from([2, 3])
g.add_edge(1, 2)
g.add_edges_from([(2, 3), (1, 3)])
print(nx.number_of_nodes(g))
print(nx.number_of_edges(g))
print(nx.degree(g, 1))
shortest_path = nx.shortest_path(g, source=1, target=3)
print(shortest_path)
# print (nx.info(g))
# print()
nx.draw(g)
plt.show()