# first attempt

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        n = len(s)
        def check(l, r):
            while 0<=l and r<n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        for i in range(len(s)):
            ans = max(ans, check(i, i), check(i, i+1), key=len)
        return ans
    

