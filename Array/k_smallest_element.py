class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []

        for i in range(len(matrix)):
            arr = matrix[i]
            for num in arr:
                res.append(num)

        return sorted(res)[k - 1]
