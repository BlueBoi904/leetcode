class MyHashMap:

    def __init__(self):
        self.hash = {}

    def put(self, key: int, value: int) -> None:
        self.hash[key] = value

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        return self.hash[key]

    def remove(self, key: int) -> None:
        if key in self.hash:
            del self.hash[key]
        return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
