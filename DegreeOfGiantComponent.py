import networkx as nx
import matplotlib.pyplot as plt


print('Number of node in ER random network is 100，The probability of connection is 0.05')
NETWORK_SIZE = 20
p = 0.1
G = nx.erdos_renyi_graph(n = NETWORK_SIZE,p = p)
ps = nx.spring_layout(G)
nx.draw(G)
plt.savefig('fig.png',bbox_inches='tight')

max_len = 0
sum_path_len = 0
for i in sorted(nx.connected_components(G), key = len, reverse = True):
    if (len(i) >= max_len):
        max_len = len(i)
    else:
        max_len = max_len
print("The degree of giant component:" + str(max_len))