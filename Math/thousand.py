class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = f"{n:,}"
        arr = [a for a in res]
        for i in range(len(arr)):
            if arr[i] == ",":
                arr[i] = "."

        return ''.join(arr)
