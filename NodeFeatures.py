#Code for generating node features for the input graphs of Graph Convolutional Network
#Author: Zahir Khan (https://sites.google.com/view/khanzahir98/home)

import torch
import network x as nx
def nodeFeatures(G): #Node features: [degree of node, local CC of node]
    features = {} #dictionary for key value pairs for (node v: [degree of v, local_clustering_coeff_of_v] )

    for n in G.nodes():
        neighbors = [x for x in G[n]]
        num_neighbors = len(neighbors) #or degree

        if num_neighbors <= 1:
           features[n] = [num_neighbors, 0.0]
        else:
            num_connected_pairs = 0
            for i in range(num_neighbors):
                for j in range(i + 1, num_neighbors):
                    if G.has_edge(neighbors[i], neighbors[j]):
                        num_connected_pairs += 1
            CC=2 * num_connected_pairs / (num_neighbors * (num_neighbors - 1))
            features[n] = [num_neighbors, round(CC,2)]

    return torch.tensor(list(features.values()))

# for a 3X3 graph the output of this function is like,
# Nodefeatures:
#   tensor([[1.0000, 0.0000],
#         [3.0000, 0.3330],
#         [2.0000, 1.0000],
#         [2.0000, 1.0000]])
