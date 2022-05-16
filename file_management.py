def load_data(file):
    # https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
    num_lines = sum(1 for line in open(file))
    data = []
    file = open(file, 'r')
    Lines = file.readlines()
    for ln in Lines:
        line = ln.split(' ')
        point1 = line[0]
        point2 = line[1]
        data.append([point1, point2])
    return data


def write_data(file, data):
    file = open(file, 'w')
    for row in data:
        point1, point2 = str(row[0]), str(row[1])
        point1 = point1.replace("(", "")
        point1 = point1.replace(")", "")
        point1 = point1.replace(" ", "")
        point2 = point2.replace("(", "")
        point2 = point2.replace(")", "")
        point2 = point2.replace(" ", "")
        file.write("[" + point1 + "] " + "[" + point2 + "]" + "\n")
    file.close()
