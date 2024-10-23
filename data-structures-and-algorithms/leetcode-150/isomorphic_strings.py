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
        s_cnt, t_cnt = 0, 0
        s_counter, t_counter = Counter(s), Counter(t)

        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                s_cnt = 0
            else:
                s_cnt += 1

            if t[i] != t[i + 1]:
                t_cnt = 0
            else:
                t_cnt += 1

            s_cnt += 1
            t_cnt += 1

            if s_cnt != t_cnt or s_counter[s[i]] < t_counter[t[i]]:
                return False

        return True


# edge cases
# assert Solution().isIsomorphic("", "") is True
# assert Solution().isIsomorphic("a", "a") is True
# assert Solution().isIsomorphic("a", "b") is True
# assert Solution().isIsomorphic("bbbaaaba", "aaabbbba") is False
assert Solution().isIsomorphic("badc", "baba") is False

assert Solution().isIsomorphic("egg", "add") is True
assert Solution().isIsomorphic("foo", "bar") is False
assert Solution().isIsomorphic("paper", "title") is True
assert Solution().isIsomorphic("ab", "aa") is False
assert Solution().isIsomorphic("ab", "ca") is True
assert Solution().isIsomorphic("ab", "cc") is False
assert Solution().isIsomorphic("ab", "cd") is True
print("Passed all tests!")
