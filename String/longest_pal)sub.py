# first attempt

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_pal = ''
        def is_palindrome(s: str):
            return s == s[::-1]

        res = [s[i: j] for i in range(len(s))
          for j in range(i + 1, len(s) + 1)]
        for item in res:
            if is_palindrome(item) and len(item) > len(longest_pal):
                longest_pal = item

        return longest_pal
    

# DP solution

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s
        
        start, size = 0, 1
        for i in range(1, len(s)):
            l, r = i - size, i + 1
            s1, s2 = s[l-1:r], s[l:r]
            
            if l - 1 >= 0 and s1 == s1[::-1]:
                start, size = l - 1, size + 2
            elif s2 == s2[::-1]:
                start, size = l, size + 1
                
        return s[start:start+size]