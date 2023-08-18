class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Get the number of rows and columns in the dungeon
        m, n = len(dungeon), len(dungeon[0])

        # Create a 2D array to store the minimum health required to reach each cell
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]

        # Set the minimum health required to reach the bottom-right cell to 1
        dp[m][n - 1] = dp[m - 1][n] = 1

        # Iterate over the cells in the dungeon in reverse order
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Calculate the minimum health required to reach the current cell
                # by taking the minimum of the health required to reach the cell on the right
                # and the cell below, and then subtracting the health change of the current cell
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])

        # Return the minimum health required to reach the top-left cell
        return dp[0][0]
