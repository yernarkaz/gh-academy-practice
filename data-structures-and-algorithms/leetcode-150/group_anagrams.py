from typing import List


class Solution:
    def count_chars(self, s: str) -> tuple:
        """
        Count the occurrences of each character in a given string.

        Args:
            s (str): The input string consisting of lowercase English letters.

        Returns:
            tuple: A tuple of length 26 where each element represents the count of a corresponding
                   character ('a' to 'z') in the input string.
        """
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups a list of strings into anagrams.

        Args:
            strs (List[str]): A list of strings to be grouped.

        Returns:
            List[List[str]]: A list of lists, where each sublist contains strings that are anagrams of each other.
        """
        res = dict()
        for s in strs:
            cnts = self.count_chars(s)
            if cnts in res:
                res[cnts].append(s)
            else:
                res[cnts] = [s]

        return list(res.values())


# edge cases
assert Solution().groupAnagrams([]) == []
assert Solution().groupAnagrams([""]) == [[""]]
assert Solution().groupAnagrams(["a"]) == [["a"]]

# test cases
assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"],
]
assert Solution().groupAnagrams([""]) == [[""]]
assert Solution().groupAnagrams(["a"]) == [["a"]]
assert Solution().groupAnagrams(["a", "b"]) == [["a"], ["b"]]
assert Solution().groupAnagrams(["a", "b", "c"]) == [["a"], ["b"], ["c"]]
assert Solution().groupAnagrams(["a", "b", "c", "d"]) == [["a"], ["b"], ["c"], ["d"]]
print("Passed all test cases!")
