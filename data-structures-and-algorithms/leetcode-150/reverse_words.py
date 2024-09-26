class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(w[::-1] for w in s.strip()[::-1].split(" ") if len(w) > 0)


print(
    Solution().reverseWords("Let's take LeetCode contest")
)  # contest LeetCode take Let's
print(Solution().reverseWords("  hello world  "))  # world hello
print(Solution().reverseWords("a good   example"))  # example good a
