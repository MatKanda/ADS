# A union by rank and path compression based
# program to detect cycle in a graph
from collections import defaultdict

# sources
# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/?fbclid=IwAR2ZniyuQ5YfR6ch4xxHIuXQ-Bp8Nlpq-x96OfZu9RXCLfRIDGK6iC2iDuQ
# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/?fbclid=IwAR0e8hV0lu912zDTjJbJOSxP7J5LbjsUFXezjQj_Jo-UTj4JvlCHGsC72OE
# https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/?fbclid=IwAR2HT6IPuXvmUbCoYfAXxYtc3gwf4gI_-KJoPbt_1ToFv-sUXEooevMru3s
# https://www.geeksforgeeks.org/union-find/?fbclid=IwAR0WcE8parPEOeIKum445ApRv64c87aooaR0sNaocVryXfVuAXHUhVyXd0o


# a structure to represent a graph
class Graph:
    def __init__(self, num_of_v):
        self.num_of_v = num_of_v
        self.edges = defaultdict(list)

    # graph is represented as an array of edges
    def add_edge(self, u, v):
        self.edges[u].append(v)


class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


# A utility function to find set of an element node(uses path compression technique)
def find(subsets, node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets, subsets[node].parent)
    return subsets[node].parent


# A function that does union of two sets of u and v(uses union by rank)
def union(subsets, u, v):
    # Attach smaller rank tree under root
    # of high rank tree(Union by Rank)
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent = v

    # If ranks are same, then make one as
    # root and increment its rank by one
    else:
        subsets[v].parent = u
        subsets[u].rank += 1


# The main function to check whether a given
# graph contains cycle or not

def is_cycle(graph):
    # Allocate memory for creating sets
    subsets = []
    prnts = []
    grphs = []

    for u in range(graph.num_of_v):
        subsets.append(Subset(u, 0))

    # Iterate through all edges of graph, find sets of both vertices of every
    # edge, if sets are same, then there is cycle in graph.
    for u in graph.edges:
        u_rep = find(subsets, u)

        for v in graph.edges[u]:
            v_rep = find(subsets, v)

            # if graf doesnt contain cycle
            if u_rep != v_rep:
                union(subsets, u_rep, v_rep)

    # graphs parent list
    for i in range(len(subsets)):
        if subsets[i].parent not in prnts:
            prnts.append(subsets[i].parent)

    # append connected graphs
    for i in range(len(prnts)):
        grph = []
        for j in range(len(subsets)):
            if subsets[j].parent == prnts[i]:
                grph.append(j)
        grphs.append(grph)
    return grphs

# This code is contributed by Neelam Yadav
