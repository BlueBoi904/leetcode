"""

2133. Check if Every Row and Column Contains All Numbers
Easy
607
37
company
Karat
instacart
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.



Example 1:


Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.
Example 2:


Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
Hence, we return false.


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
1 <= matrix[i][j] <= n

    """


def check_valid(matrix: list[list[int]]):
    # We need to check each row and column, and keep track that each number from 1-n is included in each.
    n = len(matrix)
    valid_set = set()
    # Add valid numbers from 1 to n
    for i in range(1, n + 1):
        valid_set.add(i)

    # Check each row
    for i in range(0, n):
        curr_row_seen = set()
        for j in range(0, n):
            curr = matrix[i][j]
            if curr not in valid_set or curr in curr_row_seen:
                return False
            curr_row_seen.add(curr)

    for i in range(0, n):
        curr_column_seen = set()
        for j in range(0, n):
            curr = matrix[j][i]
            if curr not in valid_set or curr in curr_column_seen:
                return False
            curr_column_seen.add(curr)

    return True


print(check_valid([[1, 2, 3], [3, 1, 2], [2, 3, 1]]))  # True

print(check_valid([[1, 1, 1], [1, 2, 3], [1, 2, 3]]))  # False
