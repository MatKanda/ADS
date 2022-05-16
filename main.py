import sys
from time import time
from Graph import Graph
from Graph import distance
from file_management import load_data
from file_management import write_data

# sources
# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/?fbclid=IwAR2ZniyuQ5YfR6ch4xxHIuXQ-Bp8Nlpq-x96OfZu9RXCLfRIDGK6iC2iDuQ
# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/?fbclid=IwAR0e8hV0lu912zDTjJbJOSxP7J5LbjsUFXezjQj_Jo-UTj4JvlCHGsC72OE
# https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/?fbclid=IwAR2HT6IPuXvmUbCoYfAXxYtc3gwf4gI_-KJoPbt_1ToFv-sUXEooevMru3s
# https://www.geeksforgeeks.org/union-find/?fbclid=IwAR0WcE8parPEOeIKum445ApRv64c87aooaR0sNaocVryXfVuAXHUhVyXd0o
# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/

if __name__ == "__main__":
    total_length = 0
    results = []
    startTime = time()

    g = Graph()
    data = load_data("graph_small.txt")
    conn_comp, g = g.create_graph(data, g)

    while True:
        main_component = conn_comp[0]
        outputPair = ""
        best_from = None
        best_to = None
        best_index = None
        best_distance = sys.maxsize
        dist = 0

        for _from in main_component:
            for indx_to, component_to in enumerate(conn_comp[1:]):
                for point_to in component_to:
                    dist = distance(_from, point_to)
                    if dist < best_distance:
                        best_distance = dist
                        best_from = _from
                        best_to = point_to
                        best_index = indx_to + 1

        # merge best result to main component
        conn_comp[0] = conn_comp[0] + conn_comp[best_index]
        # delete merged component
        del conn_comp[best_index]
        # inc total path length
        total_length += best_distance
        # append best points to results
        results.append([best_from, best_to])
        # only 1 component left -> whole graph is connected
        if len(conn_comp) <= 1:
            break

    write_data("out.txt", results)

    print(f"Compute time: {time() - startTime}")
    print(f"Path length: {total_length}")
