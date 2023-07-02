class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        chars = list(s)
        subs = []
        max_count = 0
        for i in range(len(chars)):
            for j in range(i + 1, len(chars) + 1):
                sub = ''.join(chars[i:j])
                if len(sub) <= k:
                    subs.append(sub)

        def vowel_count(s: list):
            count = 0
            for char in s:
                if char in vowels:
                    count += 1
            return count
        for sub in subs:
            temp = vowel_count(sub)
            max_count = max(temp, max_count)
        return max_count

# Optimized


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        window = res = 0
        for r in range(len(s)):
            window += s[r] in vowels
            if r >= k:
                window -= s[r - k] in vowels
            res = max(res, window)
        return res
