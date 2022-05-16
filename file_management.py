from Graph import Graph
from Graph import is_cycle


def load_data(file):
    # https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
    num_lines = sum(1 for line in open(file))
    g = Graph(num_lines)
    indx = []
    file = open(file, 'r')
    Lines = file.readlines()
    for ln in Lines:
        line = ln.split(' ')
        line[1] = line[1].strip()
        if line[0] not in indx:
            indx.append(line[0])
        if line[1] not in indx:
            indx.append(line[1])
        g.add_edge(indx.index(line[0]), indx.index(line[1]))
    g.num_of_v = len(indx)

    graphs = is_cycle(g)
    file.close()
    return graphs, indx


def write_data(file, data):
    file = open(file, 'w')
    for row in data:
        x1, y1 = str(row[0][0][0]), str(row[0][0][1])
        x2, y2 = str(row[0][1][0]), str(row[0][1][1])
        file.write("[" + x1 + "," + y1 + "] " + "[" + x2 + "," + y2 + "]" + "\n")
    file.close()
