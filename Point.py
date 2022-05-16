import math
import sys

# sources
# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/?fbclid=IwAR2ZniyuQ5YfR6ch4xxHIuXQ-Bp8Nlpq-x96OfZu9RXCLfRIDGK6iC2iDuQ
# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/?fbclid=IwAR0e8hV0lu912zDTjJbJOSxP7J5LbjsUFXezjQj_Jo-UTj4JvlCHGsC72OE
# https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/?fbclid=IwAR2HT6IPuXvmUbCoYfAXxYtc3gwf4gI_-KJoPbt_1ToFv-sUXEooevMru3s
# https://www.geeksforgeeks.org/union-find/?fbclid=IwAR0WcE8parPEOeIKum445ApRv64c87aooaR0sNaocVryXfVuAXHUhVyXd0o


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


# A utility function to find the
# distance between two points
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))


def compute_dist(graphs, indexer, starting):
    min_dist = sys.maxsize
    point_pairs = [min_dist]
    pair = [None]

    # currently picked graph
    for i in range(len(graphs[starting])):
        a = indexer[graphs[starting][i]].strip('[]').split(',')
        a[0] = int(a[0])
        a[1] = int(a[1])
        # loop other graphs
        for j in range(starting + 1, len(graphs)):
            for k in range(len(graphs[j])):
                b = indexer[graphs[j][k]].strip('[]').split(',')
                b[0] = int(b[0])
                b[1] = int(b[1])
                # pick coordinates and compute distance
                dst = dist(Point(a[0], a[1]), Point(b[0], b[1]))
                if dst < point_pairs[0]:
                    point_pairs[0] = dst
                    pair[0] = (a[0], a[1]), (b[0], b[1])

    return pair
