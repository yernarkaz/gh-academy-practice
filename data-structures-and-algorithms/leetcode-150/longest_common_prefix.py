from typing import List


class TrieNode:
    def __init__(self):
        self.nodes = [None] * 26
        self.w_end = False


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # chars[]
        # n = len(strs)
        # chars = [0] * n
        # root = TrieNode()
        # root.w_end = True

        # for i in range(n):
        #     for j, c in enumerate(strs[i]):
        #         char_ind = ord(c) - ord('a')
        #         if root.nodes[char_ind] is None:
        #             new_node = TrieNode()
        #             new_node.w_end = (j == len(strs[i]) - 1)
        #             root.nodes[char_ind] = new_node

        # print(root)

        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0 : len(prefix) - 1]

                if prefix == "":
                    return ""

        return prefix


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))  # ""
print(Solution().longestCommonPrefix(["dog", "dog", "dog"]))  # "dog"
