from operator import itemgetter


TOTAL_COUNT = 0


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
    # https://stackoverflow.com/questions/20099669/sort-multidimensional-array-based-on-2nd-element-of-the-subarray
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
        word = input_data[i][1].split("\n")[0]
        if word == input_word:
            value = int(input_data[i][0])
            return value/TOTAL_COUNT


if __name__ == "__main__":
    data = read_and_parse("dictionary.txt", "parsed_dictionary.txt")
    print(f"Total count of all values is: {TOTAL_COUNT}")
    probability = occurrence_probability(data, "the")
    print(probability)
    # print(data)
    print(find_optional_root(data))
