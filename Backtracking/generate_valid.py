"""

22. Generate Parentheses
Medium
15.7K
606
company
Uber
company
Google
company
Zenefits
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

"""


def generate_parenthesis(n: int):
    stack = []
    res = []

    def backtrack(open_count, closed_count):
        # Base case
        if open_count == closed_count == n:
            res.append(''.join(stack))
            return
        # Case to try adding a left parenthesis
        if open_count < n:
            stack.append("(")
            backtrack(open_count + 1,  closed_count)
            stack.pop()
        # Case to try adding a right parenthesis
        if closed_count < open_count:
            stack.append(')')
            backtrack(open_count,  closed_count + 1)
            stack.pop()

    backtrack(0, 0)

    return res
