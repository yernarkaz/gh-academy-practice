class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Determines if a given pattern matches a string s following the same sequence.

        Args:
            pattern (str): A string representing the pattern where each character represents a unique word.
            s (str): A string consisting of words separated by spaces.

        Returns:
            bool: True if the pattern matches the string s, False otherwise.

        Example:
            wordPattern("abba", "dog cat cat dog") -> True
            wordPattern("abba", "dog cat cat fish") -> False
            wordPattern("aaaa", "dog cat cat dog") -> False
            wordPattern("abba", "dog dog dog dog") -> False
        """

        words = s.split()

        words_dict = {}
        pattern_dict = {}

        for i, c in enumerate(pattern):
            if i >= len(words):
                return False

            if c not in pattern_dict and words[i] not in words_dict:
                pattern_dict[c] = words[i]
                words_dict[words[i]] = c

            if pattern_dict.get(c) != words[i] or words_dict.get(words[i]) != c:
                return False

        return True if len(pattern) == len(words) else False


# edge cases
assert Solution().wordPattern("", "") is True
assert Solution().wordPattern("", "dog") is False
assert Solution().wordPattern("a", "") is False
assert Solution().wordPattern("a", "dog") is True

assert Solution().wordPattern("abba", "dog cat cat dog") is True
assert Solution().wordPattern("abba", "dog cat cat fish") is False
assert Solution().wordPattern("aaaa", "dog cat cat dog") is False
assert Solution().wordPattern("abba", "dog dog dog dog") is False

print("All tests passed.")
