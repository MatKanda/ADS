import math
from collections import defaultdict
from ast import literal_eval
import sys


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


def compute_path(conn_comp):
    total_length = 0
    results = []

    while True:
        main_component = conn_comp[0]
        best_from = None
        best_to = None
        best_index = None
        best_distance = sys.maxsize

        # pick group from connected components
        for _from in main_component:
            indx_to = 0
            # pick another group from connected component for comparison
            for component_to in conn_comp[1:]:
                # take each point from picked group and compute distance between points
                for point_to in component_to:
                    dist = distance(_from, point_to)
                    if dist < best_distance:
                        best_distance = dist
                        best_from = _from
                        best_to = point_to
                        best_index = indx_to + 1
                indx_to += 1

        # append best points to results
        results.append([best_from, best_to])
        # inc total path length
        total_length += best_distance
        # merge best result to main component
        conn_comp[0] = conn_comp[0] + conn_comp[best_index]
        # delete merged component
        del conn_comp[best_index]
        # only 1 component left -> whole graph is connected
        if len(conn_comp) <= 1:
            break

    return results, total_length
