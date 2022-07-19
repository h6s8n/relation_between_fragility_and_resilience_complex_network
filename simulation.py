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

    def NumberOfGiantComponentNode(self):
        max_len = 0
        sum_path_len = 0
        for i in sorted(nx.connected_components(self.g), key=len, reverse=True):
            if (len(i) >= max_len):
                print("The degree of giant component:" + str(max_len))
                return len(i)
            else:
                print("The degree of giant component:" + str(max_len))
                return max_len

    def Resilience(self , max_len):
        S = 0
        for i in range(0, self.n_node):
            # Ng = self.NumberOfGiantComponentNode(self.g)
            Ng = max_len

            S += Ng / self.n_node
        R = (1 / self.n_node) * S
        # print(R)
        return R

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

            max_len = 0
            sum_path_len = 0
            for i in sorted(nx.connected_components(self.g), key=len, reverse=True):
                if (len(i) >= max_len):
                    max_len = len(i)
                else:
                    max_len = max_len
            print("The degree of giant component:" + str(max_len))

            nx.draw_networkx(self.g)
            plt.show()
            print('finish')

            self.g.remove_edges_from(list(edge_i))
            self.fragility += [self.Fragility()]
            self.resilience += [self.Resilience(max_len)]
            self.n_edge = self.g.number_of_edges()

        self.fragility.pop()
        self.resilience.pop()
