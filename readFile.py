def load_input(file):
    file = open(file, 'r')
    Lines = file.readlines()
    count = 0
    nb_var = 0
    nb_clauses = 0
    values_one = []
    values_two = []
    for line in Lines:
        first = int(line.split()[0])
        second = int(line.split()[1])
        if count == 0:
            nb_var = first
            nb_clauses = second
        else:
            if second == 0:
                values_one.append(first)
                values_two.append(first)
            else:
                values_one.append(first)
                values_two.append(second)
        count += 1

    return nb_var, nb_clauses, values_one, values_two
