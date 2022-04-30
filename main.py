from readFile import load_input
from KosarajuAlg import is2Satisfiable

if __name__ == "__main__":
    nb_var, nb_clauses, vals_one, vals_two = load_input("input.txt")
    print(f"nb_var: {nb_var}")
    print(f"nb_clauses: {nb_clauses}")
    print(f"vals1: {vals_one}")
    print(f"vals2: {vals_two}")

    result = is2Satisfiable(nb_var, nb_clauses, vals_one, vals_two)
    print(result)
