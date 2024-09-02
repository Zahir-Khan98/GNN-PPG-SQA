#Code of designed Graph convolutional Network models 'HVGCN' and 'NERHVGCN' for PPG SQA
#Author: Zahir Khan

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
# from torch_geometric.data import Data, DataLoader
# import torch.optim as optim

class GCNClassifier(nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super(GCNClassifier, self).__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels, add_self_loops=True, normalize=True)
        self.conv2 = GCNConv(hidden_channels, 4)
        self.conv3 = GCNConv(4,2)
        self.conv4 = GCNConv(2,1)
        #self.conv5 = GCNConv(2,1)
        self.lin = nn.Linear(1, out_channels)

    def forward(self, x, edge_index, batch):
        x = F.leaky_relu(self.conv1(x, edge_index))
        x = F.leaky_relu(self.conv2(x, edge_index))
        x = F.leaky_relu(self.conv3(x, edge_index))
        x = F.leaky_relu(self.conv4(x, edge_index))
        #x = F.leaky_relu(self.conv5(x, edge_index))
        batch_aggregated_embeddings = []
        for batch_id in batch.unique():
            graph_indices = (batch == batch_id).nonzero().squeeze(1)
            graph_embedding = torch.mean(x[graph_indices], dim=0)
            batch_aggregated_embeddings.append(graph_embedding)

        return torch.sigmoid(self.lin(torch.stack(batch_aggregated_embeddings)))
