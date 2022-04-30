"""
Edit Distance solution.
"""


def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            # If letters are same, ignore last char and take diag value for prev letters
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If letter is different, consider all possibilities and find minimum
            # min of 2 upper row vals and 1 left column val + 1
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[m][n]


def correct_text_2(input, dictionary):
    minimum = 50
    correct_word = None
    data = []

    for word in input:
        word = word.lower()
        if word in dictionary:
            data.append(word)
            continue
        for dct in dictionary:
            lcs = edit_distance(word, dct)
            if lcs < minimum:
                correct_word = dct
                minimum = lcs
            if minimum == 1:
                break
        data.append(correct_word)
        minimum = 50

    return data
