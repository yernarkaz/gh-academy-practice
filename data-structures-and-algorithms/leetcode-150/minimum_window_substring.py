from collections import Counter


class Solution:
    def is_substring(self, s_counter, t_counter):
        """
        Check if t_counter is a substring of s_counter.

        Args:
            s_counter (collections.Counter): Counter for the main string.
            t_counter (collections.Counter): Counter for the substring to check.

        Returns:
            bool: True if t_counter is a substring of s_counter, False otherwise.
        """

        for key in t_counter:
            if t_counter[key] > s_counter[key]:
                return False

        return True

    def minWindow(self, s: str, t: str) -> str:
        """
        Finds the minimum window substring in `s` that contains all the characters of `t`.

        Args:
            s (str): The source string in which to find the substring.
            t (str): The target string containing characters to be included in the window.

        Returns:
            str: The minimum window substring of `s` that contains all characters of `t`.
                 If no such window exists, returns an empty string.
        """

        # Initialize the counters
        s_counter = Counter()
        t_counter = Counter(t)

        # Initialize the pointers
        start, end = 0, 0
        min_len = float("inf")
        res = ""

        # Iterate through the string or until the start pointer is less than the end pointer
        while end < len(s) or start < end:

            # If the substring is not found, increment the end pointer
            while end < len(s) and not self.is_substring(s_counter, t_counter):
                s_counter[s[end]] += 1
                end += 1

            # If the substring is found, check if the current window is the minimum window
            if min_len > end - start and self.is_substring(s_counter, t_counter):
                min_len = end - start
                res = s[start:end]

            # If the substring is found, increment the start pointer
            s_counter[s[start]] -= 1
            start += 1

        return res


assert Solution().minimumWindow("ADOBECODEBANC", "ABC") == "BANC"
assert Solution().minimumWindow("a", "a") == "a"
assert Solution().minimumWindow("a", "aa") == ""
assert Solution().minimumWindow("a", "b") == ""
assert Solution().minimumWindow("ab", "b") == "b"
assert Solution().minimumWindow("ab", "aa") == ""
assert Solution().minimumWindow("abcdefg", "b") == "b"
assert Solution().minimumWindow("abcdefg", "bc") == "bc"
assert Solution().minimumWindow("abcdefg", "bcd") == "bcd"
assert Solution().minimumWindow("abcdefg", "bcde") == "bcde"

print("All tests passed!")
