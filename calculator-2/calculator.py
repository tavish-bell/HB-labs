"""CLI application for a prefix-notation calculator."""

from arithmetic import add, cube, divide, mod, multiply, power, square, subtract

# Replace this with your code
# pseudocode --
# while loop:
# take user input and convert it into a more readable output
# (i.e. 3 + 2 = 5)  "+ 2 3"
# tokenize this input
# if the first token is "q":
#   quit
# else:
#   includes other conditions

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": mod,
    "^": power,
    "**": square,
    "***": cube,
}


def caculator(operations):
    """
    takes user input and returns arithmetic caclulation
    """

    while True:
        user_input = input(
            "Please type the operator and numbers you want to compute(i.e. + 2 3): \n"
        )
        token = user_input.split(" ")
        operator = token[0]
        if operator == "q":
            print("bye!")
            break

        else:
            n_1 = int(token[1])
            n_2 = int(token[2])
            calculation = operations[operator](n_1, n_2)
            print(f"{n_1} {operator} {n_2} = {calculation}")
            repeat = input("would you like to make another calculation? Y/ N? ").lower()
            if repeat == "y":
                continue
            else:
                print("bye!")
                break


caculator(operations)
