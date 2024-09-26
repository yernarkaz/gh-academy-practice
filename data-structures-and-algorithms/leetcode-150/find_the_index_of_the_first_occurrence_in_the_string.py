class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # two pointers
        # robin carp

        m, n = len(needle), len(haystack)
        if m > n:
            return -1

        for i in range(n - m + 1):
            for j in range(m):
                if needle[j] != haystack[i + j]:
                    break

                if j == m - 1:
                    return i

        return -1


print(Solution().strStr("hello", "ll"))  # 2
print(Solution().strStr("aaaaa", "bba"))  # -1
