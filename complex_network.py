import scipy as sp
import scipy.io
import networkx as nx
from random import choice
import numpy as np
import matplotlib.pyplot as plt
# import warnings
# warnings.filterwarnings('ignore')
from simulation import Simulation

                                 # We call the network and attack it

Erdos = Simulation(10, 0.2)
# Erdos.Fragility()
Erdos.Attack()
# Erdos.NumberOfGiantComponentNode(Erdos.g)
#
#
plt.scatter(Erdos.fragility, Erdos.resilience)
#
#
#                                   # convert mat file
# file_path = 'fit/alfa.mat'
# scipy.io.savemat(file_path, {'alfa': Erdos.fragility}, oned_as='column')
#
# file_path = 'fit/beta.mat'
# scipy.io.savemat(file_path, {'beta': Erdos.resilience}, oned_as='column')
#
#
#                                   # plot for points
plt.xlabel("Fragility")
plt.ylabel("Resilience")
plt.show()
#
# plt.scatter([np.log10(-i) for i in Erdos.fragility],
#             [np.log10(i) for i in Erdos.resilience])
#
# plt.xlabel("Log -Fragility")
# plt.ylabel("Log Resilience")
# plt.show()
