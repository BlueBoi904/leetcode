class MagicDictionary:
    def buildDict(self, dictionary: List[str]) -> None:
        self.magic = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.magic:
            if len(word) == len(searchWord):
                c = False
                for i, letter in enumerate(word):
                    if letter != searchWord[i]:
                        if c:
                            break
                        else:
                            c = True
                else:
                    if c: return True
        return False
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)