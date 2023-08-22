from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        counts = Counter(sentence)
        return len(counts.keys()) == 26
