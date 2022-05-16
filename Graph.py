import math
from collections import defaultdict
from ast import literal_eval


# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/
# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/?fbclid=IwAR2ZniyuQ5YfR6ch4xxHIuXQ-Bp8Nlpq-x96OfZu9RXCLfRIDGK6iC2iDuQ
# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/?fbclid=IwAR0e8hV0lu912zDTjJbJOSxP7J5LbjsUFXezjQj_Jo-UTj4JvlCHGsC72OE
# https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/?fbclid=IwAR2HT6IPuXvmUbCoYfAXxYtc3gwf4gI_-KJoPbt_1ToFv-sUXEooevMru3s
# https://www.geeksforgeeks.org/union-find/?fbclid=IwAR0WcE8parPEOeIKum445ApRv64c87aooaR0sNaocVryXfVuAXHUhVyXd0o


class Graph:

    # init function to declare class variables
    def __init__(self):
        self.adj = defaultdict(set)
        self.vertices = set()

    def DFS_util(self, temp, v, visited):
        # Mark the current vertex as visited
        visited[v] = True
        # Store the vertex to list
        temp.append(v)
        # Repeat for all vertices adjacent to this vertex v
        for i in self.adj[v]:
            if visited[i] is not True:
                # Update the list
                temp = self.DFS_util(temp, i, visited)
        return temp

    # method to add an undirected edge
    def add_edge(self, v, w):
        self.adj[v].add(w)
        self.adj[w].add(v)

    # Method to retrieve connected components in an undirected graph
    def connected_components(self):
        visited = defaultdict(set)
        cc = []

        for i in self.adj:
            visited[i] = False

        for v in self.adj:
            if visited[v] == False:
                temp = []
                cc.append(self.DFS_util(temp, v, visited))
        return cc

    def create_graph(self, data, g):
        for point in data:
            point1 = literal_eval(point[0])
            point2 = literal_eval(point[1])
            g.add_edge(tuple(point1), tuple(point2))
        return g.connected_components(), g


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))
