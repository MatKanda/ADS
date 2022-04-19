from load_file import *
from LCS import *
from ED import *

if __name__ == "__main__":
    input_text_incorrect = load_text("vstup_nespravny.txt")
    input_text_correct = load_text("vstup_spravny.txt")
    dictionary = load_dict("slovnik.txt")

    print(f"Correct sentence is:\n{input_text_correct}\n")
    print(f"Incorrect sentence to be corrected is:\n{input_text_incorrect}")
    print("----------------------------------------------------------------------------------------------\n")

    # 1. option - subsequence
    data = correct_text_1(input_text_incorrect, dictionary, is_subsequence=True)
    print(data)
    errors, percentage = compare_results(input_text_correct, data)
    print(f"Number of incorrect words in subsequence method: {errors}")
    print(f"Percentage success in 'Subsequence' method: {percentage}")
    print("----------------------------------------------------------------------------------------------\n")

    # 2. option - substring
    data = correct_text_1(input_text_incorrect, dictionary, is_subsequence=False)
    print(data)
    errors, percentage = compare_results(input_text_correct, data)
    print(f"Number of incorrect words in substring method: {errors}")
    print(f"Percentage success in 'Substring' method: {percentage}")
    print("----------------------------------------------------------------------------------------------\n")

    # 3. option - edit distance
    data = correct_text_2(input_text_incorrect, dictionary)
    print(data)
    errors, percentage = compare_results(input_text_correct, data)
    print(f"Number of incorrect words in distance method: {errors}")
    print(f"Percentage success in 'Edit distance' method: {percentage}")
    print("----------------------------------------------------------------------------------------------\n")
