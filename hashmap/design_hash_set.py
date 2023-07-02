class MyHashSet:
    def __init__(self):
        self.my_set = set()

    def add(self, key: int) -> None:
        self.my_set.add(key)

    def remove(self, key: int) -> None:
        if key in self.my_set:
            self.my_set.remove(key)
            return True

        return False

    def contains(self, key: int) -> bool:
        return key in self.my_set


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
