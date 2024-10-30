from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determine if two strings s and t are isomorphic.

        Two strings s and t are isomorphic if the characters in s can be replaced to get t.
        No two characters may map to the same character, but a character may map to itself.

        Args:
            s (str): The first string to compare.
            t (str): The second string to compare.

        Returns:
            bool: True if the strings are isomorphic, False otherwise.
        """
        s_map, t_map = {}, {}

        for c_s, t_s in zip(s, t):
            if c_s not in s_map and t_s not in t_map:
                s_map[c_s] = t_s
                t_map[t_s] = c_s

            if s_map.get(c_s) != t_s or t_map.get(t_s) != c_s:
                return False

        return True


# edge cases
assert Solution().isIsomorphic("a", "a") is True
assert Solution().isIsomorphic("a", "b") is True
assert Solution().isIsomorphic("bbbaaaba", "aaabbbba") is False
assert Solution().isIsomorphic("badc", "baba") is False
assert Solution().isIsomorphic("aaeaa", "uuxyy") is False

assert Solution().isIsomorphic("egg", "add") is True
assert Solution().isIsomorphic("foo", "bar") is False
assert Solution().isIsomorphic("paper", "title") is True
assert Solution().isIsomorphic("ab", "aa") is False
assert Solution().isIsomorphic("ab", "ca") is True
assert Solution().isIsomorphic("ab", "cc") is False
assert Solution().isIsomorphic("ab", "cd") is True
print("Passed all tests!")
