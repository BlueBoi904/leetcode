class Solution:
    # Using 2 counter approach
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)

        for c in count_t.keys():
            if count_t[c] != count_s[c]:
                return c

# Using ord approach
def findTheDifference(self, s: str, t: str) -> str:
    result = 0
    for char in s + t:
        result ^= ord(char)
    return chr(result)