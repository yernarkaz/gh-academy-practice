class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines if two strings are anagrams of each other.

        An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
        typically using all the original letters exactly once.

        Args:
            s (str): The first string to compare.
            t (str): The second string to compare.

        Returns:
            bool: True if the strings are anagrams, False otherwise.
        """
        if len(s) != len(t):
            return False

        s_map, t_map = dict(), dict()
        for c_s, t_s in zip(s, t):
            s_map[c_s] = s_map.get(c_s, 0) + 1
            t_map[t_s] = t_map.get(t_s, 0) + 1

        return s_map == t_map


assert Solution().isAnagram("anagram", "nagaram") is True
assert Solution().isAnagram("rat", "car") is False
assert Solution().isAnagram("a", "ab") is False
assert Solution().isAnagram("a", "a") is True
assert Solution().isAnagram("", "") is True
assert Solution().isAnagram("a", "") is False
assert Solution().isAnagram("", "a") is False
print("Passed all test cases!")
