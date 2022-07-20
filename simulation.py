from random import choice
import numpy as np
from networkx import adjacency_spectrum
import networkx as nx
import matplotlib.pyplot as plt


class Simulation:

    def __init__(self, n, p):
        self.n_node = n
        self.p = p
        self.g = nx.erdos_renyi_graph(n, p, directed=False)
        self.n_edge = self.g.number_of_edges()
        self.resilience = []
        self.fragility = []

        self.max_len = 0
        self.sum_path_len = 0

    def NumberOfGiantComponentNode(self, g):
        # G = g
        # ps = nx.spring_layout(G)
        # nx.draw(G)
        # plt.savefig('fig.png', bbox_inches='tight')

        max_len = 0
        sum_path_len = 0
        for i in sorted(nx.connected_components(g), key=len, reverse=True):
            if (len(i) >= max_len):
                max_len = len(i)
                # print("The degree of giant component:" + str(max_len))
                return max_len
            else:
                # print("The degree of giant component:" + str(max_len))
                return max_len

    def Resilience(self, gc):
        S = 0
        for i in range(1, self.n_node + 1):
            # Ng = self.NumberOfGiantComponentNode(self.g)
            ng = gc
            # print("step:" + str(self.n_node))
            # print("self.n_node:" + str(i))
            S += ng / i
            # print("sum sigma:" + str(S))
        result = (1 / self.n_node) * S
        # print(R)
        return result

    def Fragility(self):
        # adj_matrix = nx.adjacency_matrix(self.g)
        eig_val = adjacency_spectrum(self.g)
        # print(eig_val)
        # A = nx.normalized_laplacian_matrix(self.g).A
        # eig_val = np.linalg.eigvals(A)
        d_max = max(abs(eig_val.real))
        f = -d_max
        # print(f)
        return f

    # def SelectRandomlyNode(self):

    def Attack(self):

        while self.n_edge >= 1:
            node_i = choice([n for n, d in self.g.degree() if d >= 1])
            print('start')
            print(node_i)
            #
            nx.draw_networkx(self.g)
            plt.show()

            edge_i = self.g.edges(node_i)
            self.g.remove_edges_from(list(edge_i))

            gc = self.NumberOfGiantComponentNode(self.g)
            print("The degree of giant component:")
            print(gc)

            nx.draw_networkx(self.g)
            plt.show()
            print('finish')

            self.g.remove_edges_from(list(edge_i))
            self.fragility += [self.Fragility()]
            self.resilience += [self.Resilience(gc)]
            self.n_edge = self.g.number_of_edges()

        self.fragility.pop()
        self.resilience.pop()
