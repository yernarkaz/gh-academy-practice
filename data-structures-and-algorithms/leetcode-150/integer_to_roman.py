class Solution:
    def intToRoman(self, num: int) -> str:
        rtoi_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        itor_map = {v: k for k, v in rtoi_map.items()}

        # 3749
        # 3000 + 700 + 40 + 9
        # MMM + DCC + XL + IX

        # 58
        # 50 + 8
        # LVIII

        # 1994
        # 1000 + 900 + 90 + 4
        # M + CM + XC + IV

        res = []
        denom = 10

        # split number into digits
        while num > 0:
            # get the remainder of the division
            rem = num % denom

            # if the remainder is 0, move to the next digit
            if rem == 0:
                denom *= 10
                continue

            # subtract the remainder from the number
            num -= rem

            # 9, 40
            # if the remainder is 4 or 9, append the corresponding pair of roman numerals
            if rem // (denom / 10) in [4, 9]:
                res.append(itor_map[denom // 10] + itor_map[rem + denom // 10])
            else:

                subnum = []

                # if the remainder is not 4 or 9, append the corresponding roman numerals
                while rem not in itor_map:
                    rem -= denom // 10

                    subnum.append(itor_map[denom // 10])

                subnum.append(itor_map[rem])
                res.append("".join(reversed(subnum)))

            denom *= 10

        return "".join(reversed(res))


print(Solution().intToRoman(3))  # III
print(Solution().intToRoman(4))  # IV
print(Solution().intToRoman(9))  # IX
print(Solution().intToRoman(58))  # LVIII
print(Solution().intToRoman(1994))  # MCMXCIV
print(Solution().intToRoman(3749))  # MMMMDCCXLIX
print(Solution().intToRoman(3999))  # MMMCMXCIX
print(Solution().intToRoman(399))  # CCCXC
print(Solution().intToRoman(300))  # CCC
print(Solution().intToRoman(30))  # XXX
