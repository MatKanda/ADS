from operator import itemgetter


TOTAL_COUNT = 0
root_table = [[]]
cost_table = [[]]


def remove_end(word):
    return word.split("\n")[0]


def read_and_parse(input_file, output_file):
    global TOTAL_COUNT
    print("Parsing document...")

    parsed_data = []

    # open and close to clear data if already exists
    open(output_file, "w").close()

    # open file to read
    file1 = open(input_file, 'r')
    Lines = file1.readlines()

    # iterate the lines read from file
    for line in Lines:
        value = int(line.split(" ")[0])
        TOTAL_COUNT += value
        word = line.split(" ")[1]
        if value > 50_000:
            tmp = str(value) + " " + word
            parsed_data.append([value, word])

    parsed_data = lex_arrangement(parsed_data, output_file)
    print("Document parsed.")
    return parsed_data


def lex_arrangement(input_data, output_file):
    # sort by word name
    input_data = sorted(input_data, key=itemgetter(1))

    # open file to read
    f = open(output_file, "a")
    for i in range(len(input_data)):
        tmp = str(input_data[i][0]) + " " + str(input_data[i][1])
        f.write(tmp)
    f.close()
    return input_data


def occurrence_probability(input_data, input_word):
    for i in range(len(input_data)):
        # split -> remove end of line character
        # word = input_data[i][1].split("\n")[0]
        word = remove_end(input_data[i][1])
        if word == input_word:
            value = int(input_data[i][0])
            return value/TOTAL_COUNT


def find_best_root(input_data):
    """
    Find best tree root for data from "parsed_dictionary.txt"
    """
    results = []
    # try all the words as tree root
    for i in range(len(input_data)):

        # first word, no words on the left side, compute only right side
        if i == 0:
            level = 1
            cost = 0
            for j in range(len(input_data)):
                # split -> remove end of line character
                word = remove_end(input_data[j][1])
                # occurrence * level (depth)
                current_cost = occurrence_probability(input_data, word) * level
                cost += current_cost
                level += 1
            results.append(cost)
        # last word, no other words on right side, compute only left side
        elif i == len(input_data)-1:
            level = 1
            cost = 0
            for j in reversed(range(len(input_data))):
                # split -> remove end of line character
                word = remove_end(input_data[j][1])
                # occurrence * level (depth)
                current_cost = occurrence_probability(input_data, word) * level
                cost += current_cost
                level += 1
            results.append(cost)
        # there are words on both sides
        else:
            level = 1
            cost = 0

            # compute root
            word = remove_end(input_data[i][1])
            # occurrence * level (depth)
            current_cost = occurrence_probability(input_data, word) * level
            cost += current_cost

            # compute left side
            level = 2
            for j in reversed(range(0, i)):
                # split -> remove end of line character
                word = remove_end(input_data[j][1])
                # occurrence * level (depth)
                current_cost = occurrence_probability(input_data, word) * level
                cost += current_cost
                level += 1

            # compute right side
            level = 2
            for j in range(i+1, len(input_data)):
                # split -> remove end of line character
                word = remove_end(input_data[j][1])
                # occurrence * level (depth)
                current_cost = occurrence_probability(input_data, word) * level
                cost += current_cost
                level += 1
            results.append(cost)

    print(results)
    index = results.index(min(results))
    print(f"Best root word is: {input_data[index][1]}Cost is :{results[index]}")
    return input_data[index][1]


def increasing_depth(start, end, input_data):
    count = 0
    for i in range(start, end):
        count += occurrence_probability(input_data, remove_end(input_data[i][1]))
    return count


def create_cost_and_root_table(input_data):
    global root_table
    global cost_table
    n = len(input_data)
    root_table = [[0 for i in range(n)] for i in range(n)]
    cost_table = [[0 for i in range(n)] for i in range(n)]

    # init
    for i in range(1, n):
        cost_table[i][i] = occurrence_probability(input_data, remove_end(input_data[i][1]))
        root_table[i][i] = i

    for d in range(1, n-1):
        for i in range(n-d):
            j = d + i
            _min = float('inf')
            tmp = 0
            for l in range(i, j):
                # combination of left subtree + right subtree
                tmp = cost_table[i][l - 1] + cost_table[l + 1][j]
                # new min, update
                if tmp < _min:
                    _min = tmp
                    # save root that gave us min value
                    root_table[i][j] = l
            cost_table[i][j] = tmp + increasing_depth(i, j, input_data)


if __name__ == "__main__":
    data = read_and_parse("dictionary.txt", "parsed_dictionary.txt")
    print(f"Total count of all values is: {TOTAL_COUNT}")
    probability = occurrence_probability(data, "the")
    print(probability)
    root = find_best_root(data)
    create_cost_and_root_table(data)
    print(cost_table)
