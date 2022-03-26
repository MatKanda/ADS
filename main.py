from operator import itemgetter
import sys
from Node import Node
import math


TOTAL_COUNT = 0
allData = []


def remove_end(word):
    return word.split("\n")[0]


def get_word_by_index(input_data, index):
    return input_data[index][1]


def read_and_parse(input_file, output_file):
    global TOTAL_COUNT
    global allData
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
        allData.append([value, word])
        if value > 50_000:
            tmp = str(value) + " " + word
            parsed_data.append([value, word])

    allData = sorted(allData, key=itemgetter(1))

    # open file to read
    open("dictionary.txt", "w").close()
    f = open("dictionary.txt", "a")
    for i in range(len(allData)):
        tmp = str(allData[i][0]) + " " + str(allData[i][1])
        f.write(tmp)
    f.close()

    parsed_data = lex_arrangement(parsed_data, output_file)
    print("Document parsed.\n")
    return parsed_data


def lex_arrangement(input_data, output_file):
    print("Doing alphabeticall arrange...")
    # sort by word name
    input_data = sorted(input_data, key=itemgetter(1))

    # open file to read
    f = open(output_file, "a")
    for i in range(len(input_data)):
        tmp = str(input_data[i][0]) + " " + str(input_data[i][1])
        f.write(tmp)
    f.close()
    print("Alphabeticall arrange done.")
    return input_data


def occurrence_probability(input_data, input_word):
    for i in range(len(input_data)):
        # split -> remove end of line character
        # word = input_data[i][1].split("\n")[0]
        word = remove_end(input_data[i][1])
        if word == input_word:
            value = int(input_data[i][0])
            return value / TOTAL_COUNT


def dummy_key_cost(data):
    print("Computing dummy keys costs...")
    q = []
    inc = 0
    q.append(0)
    end = 0
    for i in range(len(data) - 1):
        sum = 0
        start = remove_end(data[i][1])
        end = remove_end(data[i+1][1])
        for j in range(len(allData)):
            if remove_end(allData[j][1]) == start:
                start = j
                inc = +1
            if remove_end(allData[j][1]) == end:
                end = j
                inc += 1
            if inc == 2:
                inc = 0
                break

        for j in range(start+1, end):
            sum += int(allData[j][0])
        sum = sum / TOTAL_COUNT
        q.append(sum)

    sum = 0
    for j in range(end+1, len(allData)):
        sum += int(allData[j][0])
    sum = sum / TOTAL_COUNT
    q.append(sum)

    print("Dummy keys costs computed.\n")
    return q


def key_cost(data):
    n = len(data)
    costs = [occurrence_probability(data, remove_end(data[i][1])) for i in range(n)]
    costs.append(0)
    return costs


def compute_q(i, j, data):
    sum = 0
    for index in range(i, j + 1):
        sum += data[index]
    return sum


def compute_p(i, j, data):
    sum = 0
    for index in range(i, j):
        sum += data[index]
    return sum


def create_tree(keys, k, i, j):
    r = k[i][j]
    if i == j:
        root = Node(keys[r])

    else:
        root = Node(keys[r])
        if i <= r - 1:
            root.left = create_tree(keys, k, i, r - 1)
        if r + 1 <= j:
            root.right = create_tree(keys, k, r + 1, j)

    return root


def create_tables(data, p, q):
    n = len(data)
    keys = [remove_end(data[i][1]) for i in range(n)]
    keys.insert(0, "garbage")
    p.insert(0, 0)
    n += 1

    cost_table = [[0 for j in range(n)] for i in range(n)]
    w = [[0 for j in range(n + 1)] for i in range(n + 1)]
    root_table = [[0 for j in range(n)] for i in range(n)]

    for i in range(1, n + 1):
        cost_table[i - 1][i - 1] = q[i - 1]
        w[i - 1][i - 1] = q[i - 1]

    for d in range(1, n):
        for i in range(1, n - d + 1):
            j = i + d - 1
            cost_table[i - 1][j] = sys.maxsize
            w[i - 1][j] = w[i - 1][j - 1] + p[j] + q[j]
            for r in range(i, j + 1):
                left = cost_table[i - 1][r - 1]
                right = cost_table[r + 1 - 1][j]
                tmp = left + right + w[i - 1][j]
                if tmp < cost_table[i - 1][j]:
                    cost_table[i - 1][j] = tmp
                    root_table[i][j] = r

    print("Tables created.\n")
    print("Creating binary search tree...")
    return create_tree(keys, root_table, 1, n - 1)


def number_of_comparisons(tree, word_to_search):
    counter = 0
    word = tree.get_data()
    while True:
        counter += 1
        if word == word_to_search:
            print(f"Number of comparisons for word '{word_to_search}' was: {counter}")
            break
        else:
            result = sorted([word, word_to_search])
            if result[0] == word:
                tree = tree.get_right_child()
                if tree is None:
                    print(f"Number of comparisons for word (not in tree) '{word_to_search}' was: {counter+1}")
                    break
                word = tree.get_data()
            else:
                tree = tree.get_left_child()
                if tree is None:
                    print(f"Number of comparisons for word (not in tree)'{word_to_search}' was: {counter+1}")
                    break
                word = tree.get_data()


def print_tree(rootnode):
    thislevel = [rootnode]
    num_levels = 0
    while thislevel:
        level = []
        num_levels += 1
        nextlevel = list()
        for n in thislevel:
            level.append(n.data)
            if n.left:
                nextlevel.append(n.left)
            if n.right:
                nextlevel.append(n.right)
        print(20*''+'Level '+str(num_levels)+73*'')
        print(level)
        thislevel = nextlevel


if __name__ == "__main__":
    data = read_and_parse("dictionary.txt", "parsed_dictionary.txt")
    q_probs = dummy_key_cost(data)
    p_probs = key_cost(data)

    probability = occurrence_probability(data, "the")

    root = create_tables(data, p_probs, q_probs)
    print("Binary search tree created.\n")
    print_tree(root)
    while True:
        word = input("Word: ")
        number_of_comparisons(root, word)
