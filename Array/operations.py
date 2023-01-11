"""

2011. Final Value of Variable After Performing Operations
Easy
995
136
company
Bloomberg
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.



"""


def final_value_after_operations(operations: list[str]):
    x = 0
    plus_operations = {
        "X++": True,
        "++X": True
    }

    minus_operations = {
        "--X": True,
        "X--": True
    }

    for operation in operations:
        if operation in plus_operations:
            x += 1
        if operation in minus_operations:
            x -= 1

    return x
