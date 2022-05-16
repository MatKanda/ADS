import time
from Point import compute_dist
from file_management import load_data
from file_management import write_data

# sources
# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/?fbclid=IwAR2ZniyuQ5YfR6ch4xxHIuXQ-Bp8Nlpq-x96OfZu9RXCLfRIDGK6iC2iDuQ
# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/?fbclid=IwAR0e8hV0lu912zDTjJbJOSxP7J5LbjsUFXezjQj_Jo-UTj4JvlCHGsC72OE
# https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/?fbclid=IwAR2HT6IPuXvmUbCoYfAXxYtc3gwf4gI_-KJoPbt_1ToFv-sUXEooevMru3s
# https://www.geeksforgeeks.org/union-find/?fbclid=IwAR0WcE8parPEOeIKum445ApRv64c87aooaR0sNaocVryXfVuAXHUhVyXd0o
if __name__ == "__main__":
    graphs, indx = load_data("graph_small.txt")

    min_pair_dist = []
    all_dist = 0
    start_compute = time.time()
    for i in range(len(graphs) - 1):
        # if i == 3:
        #     print(0)
        min_pair_dist.append(compute_dist(graphs, indx, i))
    end_compute = time.time()

    write_data("out.txt", min_pair_dist)

    print(f"Compute time was: {end_compute - start_compute}")
