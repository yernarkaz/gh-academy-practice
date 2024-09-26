class Solution:
    def romanToInt(self, s: str) -> int:
        rtoi_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # XIV

        res = 0
        prev_c = None
        for c in reversed(s):
            if prev_c is not None:
                if rtoi_map[c] < rtoi_map[prev_c]:
                    res -= rtoi_map[c]
                else:
                    res += rtoi_map[c]
            else:
                res = rtoi_map[c]

            prev_c = c

        return res


print(Solution().romanToInt("III"))  # 3
print(Solution().romanToInt("IV"))  # 4
print(Solution().romanToInt("IX"))  # 9
print(Solution().romanToInt("LVIII"))  # 58
print(Solution().romanToInt("MCMXCIV"))  # 1994
print(Solution().romanToInt("MMMCMXCIV"))  # 3994
