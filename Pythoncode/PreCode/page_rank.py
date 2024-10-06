import networkx as nx
import random
import matplotlib.pyplot as plt
l=[[2,6],[4,5],[2,4]]
G=nx.Graph()
G.add_edges_from(l)
nx.draw(G)
# plt.show()
p=nx.pagerank(G)
print(p)
