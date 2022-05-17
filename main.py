from time import time
from Graph import Graph
from file_management import load_data
from file_management import write_data
from Graph import compute_path

# sources
# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/?fbclid=IwAR2ZniyuQ5YfR6ch4xxHIuXQ-Bp8Nlpq-x96OfZu9RXCLfRIDGK6iC2iDuQ
# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/?fbclid=IwAR0e8hV0lu912zDTjJbJOSxP7J5LbjsUFXezjQj_Jo-UTj4JvlCHGsC72OE
# https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/?fbclid=IwAR2HT6IPuXvmUbCoYfAXxYtc3gwf4gI_-KJoPbt_1ToFv-sUXEooevMru3s
# https://www.geeksforgeeks.org/union-find/?fbclid=IwAR0WcE8parPEOeIKum445ApRv64c87aooaR0sNaocVryXfVuAXHUhVyXd0o
# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/

if __name__ == "__main__":
    startTime = time()

    g = Graph()
    data = load_data("graph_small.txt")
    # create connected components - connected groups
    conn_comp, g = g.create_graph(data, g)

    results, total_length = compute_path(conn_comp)

    write_data("out.txt", results)

    print(f"Compute time: {time() - startTime}")
    print(f"Path length: {total_length}")
