from load_file import *
from LCS import *


if __name__ == "__main__":
    input_text_incorrect = load_text("vstup_nespravny.txt")
    input_text_correct = load_text("vstup_spravny.txt")
    dictionary = load_dict("slovnik.txt")

    data = correct_text(input_text_incorrect, dictionary)
    print(data)
    print(f"Number of incorrect words: {compare_results(input_text_correct, data)}")
