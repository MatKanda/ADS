from operator import itemgetter
import sys
import numpy as np
import pandas as pd


TOTAL_COUNT = 0
root_table = [[]]
cost_table = [[]]


def remove_end(word):
    return word.split("\n")[0]


def get_word_by_index(input_data, index):
    return input_data[index][1]


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
    for i in range(start, end+1):
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
        cost_table[i][i-1] = 0
        cost_table[i][i] = occurrence_probability(input_data, remove_end(input_data[i][1]))
        root_table[i][i] = i
    # cost_table[n+1][n] = 0

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


def print_binary_search_tree(root, key, i, j, parent, is_left):
    """
    Recursive function to print a BST from a root table.

    >>> key = [3, 8, 9, 10, 17, 21]
    >>> root = [[0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 3], [0, 0, 2, 3, 3, 3], \
                [0, 0, 0, 3, 3, 3], [0, 0, 0, 0, 4, 5], [0, 0, 0, 0, 0, 5]]
    >>> print_binary_search_tree(root, key, 0, 5, -1, False)
    8 is the root of the binary search tree.
    3 is the left child of key 8.
    10 is the right child of key 8.
    9 is the left child of key 10.
    21 is the right child of key 10.
    17 is the left child of key 21.
    """
    if i > j or i < 0 or j > len(root) - 1:
        return

    node = root[i][j]
    if parent == -1:  # root does not have a parent
        print(f"{key[node]} is the root of the binary search tree.")
    elif is_left:
        print(f"{key[node]} is the left child of key {parent}.")
    else:
        print(f"{key[node]} is the right child of key {parent}.")

    print_binary_search_tree(root, key, i, node - 1, key[node], True)
    print_binary_search_tree(root, key, node + 1, j, key[node], False)


def create_tables_ep2(data):
    global cost_table
    global root_table
    n = len(data)

    keys = [data[i][1] for i in range(n)]
    freqs = [occurrence_probability(data, remove_end(data[i][1])) for i in range(n)]

    # This 2D array stores the overall tree cost (which's as minimized as possible);
    # for a single key, cost is equal to frequency of the key.
    cost_table = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]
    # sum[i][j] stores the sum of key frequencies between i and j inclusive in nodes
    # array
    sum = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]
    # stores tree roots that will be used later for constructing binary search tree
    root_table = [[i if i == j else 0 for j in range(n)] for i in range(n)]

    for interval_length in range(2, n + 1):
        for i in range(n - interval_length + 1):
            j = i + interval_length - 1

            cost_table[i][j] = sys.maxsize  # set the value to "infinity"
            sum[i][j] = sum[i][j - 1] + freqs[j]

            # Apply Knuth's optimization
            # Loop without optimization: for r in range(i, j + 1):
            for r in range(root_table[i][j - 1], root_table[i + 1][j] + 1):  # r is a temporal root
                # if r == i, there is no left subtree
                left = cost_table[i][r - 1] if r != i else 0  # optimal cost for left subtree
                # if r == j, there is no right subtree
                right = cost_table[r + 1][j] if r != j else 0  # optimal cost for right subtree
                cost = left + sum[i][j] + right

                if cost_table[i][j] > cost:
                    cost_table[i][j] = cost
                    root_table[i][j] = r

    # print("Binary search tree nodes:")
    # for node in data:
    #     print(node)
    #
    # print(f"\nThe cost of optimal BST for given tree nodes is {cost_table[0][n - 1]}.")
    # print_binary_search_tree(root_table, keys, 0, n - 1, -1, False)


if __name__ == "__main__":
    data = read_and_parse("dictionary.txt", "parsed_dictionary.txt")
    print(f"Total count of all values is: {TOTAL_COUNT}")
    probability = occurrence_probability(data, "the")
    print(probability)
    # root = find_best_root(data)
    # create_cost_and_root_table(data)
    create_tables_ep2(data)
    # create_tables_ep3(data)
    print(f"ideal root index: {root_table[0][150]}")
    print(f"ideal root word: {get_word_by_index(data, root_table[0][150])}")
    # print(cost_table)
