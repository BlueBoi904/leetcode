"""

Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even you have to divide it by 2, oterwise, you have to subtract 1 from it.

"""


def number_of_steps(num: int):
    # Create helper function
    def helper(curr_num, step_count=0):
        # Develop a base case
        if curr_num == 0:
            return step_count
        # Curr number is even
        if curr_num % 2 == 0:
            return helper(curr_num / 2, step_count + 1)

        else:
            return helper(curr_num - 1, step_count + 1)

    return helper(num)


# Create test cases
print(number_of_steps(14))  # => 6
print(number_of_steps(8))  # => 4
