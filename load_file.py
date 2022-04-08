def load_text(path):
    data = []
    f = open(path, "r")
    Lines = f.read().splitlines()
    for line in Lines:
        strip_lines = line.strip()
        data = strip_lines.split()
    return data


def load_dict(path):
    data = []
    f = open(path, "r")
    Lines = f.readlines()
    for line in Lines:
        data.append(line.split("\n")[0])
    return data


def compare_results(x, y):
    counter = 0
    for i in range(len(x)):
        if x[i].lower() != y[i].lower():
            counter += 1
    return counter
