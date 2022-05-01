from readFile import load_input
from KosarajuAlg import is2_satisfiable

if __name__ == "__main__":
    nb_var, nb_clauses, vals_one, vals_two = load_input("input.txt")
    print(f"nb_var: {nb_var}")
    print(f"nb_clauses: {nb_clauses}")
    # print(f"vals1: {vals_one}")
    # print(f"vals2: {vals_two}")

    result, solutions = is2_satisfiable(nb_var, nb_clauses, vals_one, vals_two)
    print(result)
    if solutions is not None:
        for i in range(len(solutions)):
            print(f"x{i+1}: {solutions[i]}")
