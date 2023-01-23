import itertools

POSSIBLE_OPERATORS = ["+", "-", "*", "/"]
POSSIBLE_OPEN = "O"
POSSIBLE_CLOSE = "C"
TARGET_VALUE = 10


def _valuate(string):
    return eval(string.replace("C", "").replace("O", ""))


def check_ops(permutation, ops):
    evaluation_string = f"{POSSIBLE_OPEN}{permutation[0]}"
    for i in range(1, len(permutation)):
        evaluation_string += (
            f"{POSSIBLE_CLOSE}{ops[i-1]}{POSSIBLE_OPEN}{permutation[i]}"
        )
    evaluation_string += POSSIBLE_CLOSE

    if _valuate(evaluation_string) == TARGET_VALUE:
        print("SUCCESS!!")

    for open_bracket in range(len(evaluation_string)):
        if evaluation_string[open_bracket] != POSSIBLE_OPEN:
            continue
        current_string = (
            evaluation_string[:open_bracket]
            + "("
            + evaluation_string[open_bracket + 1 :]
        )
        for close_bracket in range(open_bracket + 3, len(current_string)):
            if current_string[close_bracket] != POSSIBLE_CLOSE:
                continue
            t_string = (
                current_string[:close_bracket] + ")" + current_string[close_bracket:]
            )
            try:
                if _valuate(t_string) == TARGET_VALUE:
                    print("SUCCESS!!")
                    print(t_string.replace("C", "").replace("O", ""))
                    return True
            except ZeroDivisionError:
                pass


def check_permutation(permutation):
    # checks whether there is a solution for this particular permutation
    for op1 in POSSIBLE_OPERATORS:
        for op2 in POSSIBLE_OPERATORS:
            for op3 in POSSIBLE_OPERATORS:
                if check_ops(permutation, [op1, op2, op3]):
                    return True


def main(input):
    for permutation in itertools.permutations(input):
        if check_permutation(permutation):
            print(f"found result in permutation: {permutation}")
            break


if __name__ == "__main__":
    input_str = input("Enter the numbers, splitted by spaces: ").strip(" ")
    main(input_str.split(" "))
