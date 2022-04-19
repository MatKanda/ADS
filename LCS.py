"""
Longest Common Substring/Subsequence
"""


def longest_common_substring(x, y):
    m = len(x)
    n = len(y)
    table = [[0 for i in range(n + 1)] for j in range(m + 1)]
    result = 0

    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                table[i][j] = 0
            elif (x[i - 1] == y[j - 1]):
                table[i][j] = table[i - 1][j - 1] + 1
                result = max(result, table[i][j])
            else:
                table[i][j] = 0
    return result


def longest_common_subsequence(x, y):
    m = len(x)
    n = len(y)
    table = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table[m][n]


def correct_text_1(input, dictionary, is_subsequence: bool):
    maximum = 0
    correct_word = None
    data = []

    for word in input:
        word = word.lower()
        if word in dictionary:
            data.append(word)
            continue
        for dct in dictionary:
            if is_subsequence:
                lcs = longest_common_subsequence(word, dct)
            else:
                lcs = longest_common_substring(word, dct)
            if lcs > maximum:
                correct_word = dct
                maximum = lcs
            if maximum == len(word):
                break
        data.append(correct_word)
        maximum = 0

    return data
