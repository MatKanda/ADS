def load_input(file):
    file = open(file, 'r')
    Lines = file.readlines()
    count = 0
    nb_var = 0
    nb_clauses = 0
    values_one = []
    values_two = []
    for line in Lines:
        if count == 0:
            nb_var = int(line.split()[0])
            nb_clauses = int(line.split()[1])
        else:
            values_one.append(int(line.split()[0]))
            values_two.append(int(line.split()[1]))
            # tmp_array = []
            # tmp = line.split()[0]
            # if tmp != "0":
            #     tmp_array.append(tmp)
            # tmp = line.split()[1]
            # if tmp != "0":
            #     tmp_array.append(tmp)
            # values.append(tmp_array)
        count += 1

    return nb_var, nb_clauses, values_one, values_two
