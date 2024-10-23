from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        diff = Counter(ransomNote) - Counter(magazine)
        return not diff


assert Solution().canConstruct("a", "b") is False
assert Solution().canConstruct("aa", "ab") is False
assert Solution().canConstruct("aa", "aab") is True
assert Solution().canConstruct("aazxc", "aab") is False
print("Passed all tests!")
