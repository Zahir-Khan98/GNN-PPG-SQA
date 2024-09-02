#Code for transferring time series signal (given in list format) to HVG (Horizontal Visibility Graph)
#Author: Zahir Khan (https://sites.google.com/view/khanzahir98/home)

import networkx as nx
def HVG(TS):   #TS=list of 1D time series signals.
    G=nx.Graph()
    G.add_node(0)
    for i in range(len(TS)-1):
        G.add_node(i+1)
        G.add_edge(i,i+1)
    for i in range(len(TS)-2):
        M=TS[i+1]
        for j in range(i+2,len(TS)):
            if M>TS[i]:
                break
            if TS[i]>M and TS[j]>M:
                G.add_edge(i,j)
                M=TS[j]
    return G
