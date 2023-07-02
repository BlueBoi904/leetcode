"""

1876. Substrings of Size Three with Distinct Characters
Easy
1.1K
30
company
Amazon
company
Quora
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
 

Constraints:

1 <= s.length <= 100
s​​​​​​ consists of lowercase English letters.


"""

from collections import Counter

# First attempt

def count_good_subs(s: str):
    subs = []
    count = 0
    def no_repeat(sub: str):
        counts = Counter(sub) 
        for char in counts:
            count = counts[char]
            if count > 1:
                return False
        return True
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if len(sub) == 3:
                subs.append(sub)
   
    for sub in subs:
        if no_repeat(sub):
            count += 1

    return count
        
            
    
                    

            


print(count_good_subs("xyzzaz"))
print(count_good_subs("aababcabc"))


