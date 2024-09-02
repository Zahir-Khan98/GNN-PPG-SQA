# Code for generating graphs from time series signals using NERHVG algorithms
# Author: Zahir Khan (https://sites.google.com/view/khanzahir98/home)
import networkx as nx
from NVT_paramsFor_NERHVG import Average_alpha
def NERHVG(TS):
    TS=normalise(TS)
    Avg_alpha=Average_alpha(TS,10,25)
    G=nx.Graph()
    G.add_node(0)
    for i in range(len(TS)-1):
        G.add_node(i+1)
        if abs(TS[i]-TS[i+1])<Avg_alpha[i]:
            G.add_edge(i,i+1)
    for i in range(len(TS)-2):
        M=TS[i+1]
        for j in range(i+2,len(TS)):
            if M>=TS[i]:
                break
            if TS[i]>M and TS[j]>M:
                G.add_edge(i,j)
                M=TS[j]

    return G
