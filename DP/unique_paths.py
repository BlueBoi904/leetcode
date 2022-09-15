"""

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

"""

# Possible moves right or down at any point in time.


def uniquePaths(m, n):

    dp = [[None for _ in range(n)] for _ in range(m)]

    def dfs(x, y):
        if x > m-1 or y > n-1:
            return 0
        elif dp[x][y]:
            return dp[x][y]
        elif x == m-1 and y == n-1:
            return 1
        else:
            dp[x][y] = dfs(x+1, y) + dfs(x, y+1)
            return dp[x][y]

    return dfs(0, 0)
