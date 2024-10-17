class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        left, right = 0, 0
        characters = set()

        while right < len(s):
            while s[right] in characters:
                characters.remove(s[left])
                left += 1

            characters.add(s[right])
            res = max(res, right - left + 1)
            right += 1

        return res


assert Solution().lengthOfLongestSubstring("") == 0
assert Solution().lengthOfLongestSubstring(" ") == 1
assert Solution().lengthOfLongestSubstring("au") == 2
assert Solution().lengthOfLongestSubstring("aab") == 2
assert Solution().lengthOfLongestSubstring("dvdf") == 3
assert Solution().lengthOfLongestSubstring("pwwkew") == 3
assert Solution().lengthOfLongestSubstring("bbbbb") == 1
assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("tmmzuxt") == 5
print("Passed all test cases!")
