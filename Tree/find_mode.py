class Solution:
    def findMode(self, root) -> list[int]:
        hashmap = {}
        res = []

        def dfs_ele_freq(root):
            if not root:
                return None

            if root.val not in hashmap:
                hashmap[root.val] = 1
            else:
                hashmap[root.val] += 1

            dfs_ele_freq(root.left)
            dfs_ele_freq(root.right)

        dfs_ele_freq(root)
        mode_list = max(list(hashmap.values()))
        for key, value in hashmap.items():
            if value == mode_list:
                res.append(key)

        return res
