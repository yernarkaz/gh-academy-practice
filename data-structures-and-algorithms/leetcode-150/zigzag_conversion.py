class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        P   A   H   N
        A P L S I I G
        Y   I   R
        0   4   8    12
        1 3 5 7 9 11 13
        2   6   10
        """

        """
        P     I     N
        A   L S   I G
        Y A   H R 
        P     I

        0     6       12
        1   5 7    11 13
        2 4   8 10
        3     9  
        """

        """
        abcdefg numRows=2
        a c e g
        b d f
        """

        # if numRows is 1, return the string as is
        if numRows == 1:
            return s

        n = len(s)
        res = []

        # initialize the step to jump between the diagonals
        step = 2 * (numRows - 1)  # if 4 => 6, if 3 => 4, if 5 => 8

        # iterate over the number of rows
        for i in range(numRows):
            # iterate over the string beginning at the current row
            j = i
            while j < n:
                # append the current character to the result
                res.append(s[j])

                # if the row is not the first or the last row, append the diagonal character to the result
                if 0 < i < numRows - 1:
                    # calculate the diagonal character index
                    step_diag = j + (step - 2 * i)

                    if step_diag < n:
                        res.append(s[step_diag])

                # move to the next character in the current row
                j += step

        return "".join(res)


print(Solution().convert("PAYPALISHIRING", 3))  # "PAHNAPLSIIGYIR"
print(Solution().convert("PAYPALISHIRING", 4))  # "PINALSIGYAHRPI"
print(Solution().convert("A", 1))  # "A"
print(Solution().convert("AB", 1))  # "AB"
print(Solution().convert("ABC", 1))  # "ABC"
print(Solution().convert("ABC", 2))  # "ACB"
