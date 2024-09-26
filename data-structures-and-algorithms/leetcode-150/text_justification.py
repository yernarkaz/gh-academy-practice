from typing import List


class Solution:
    def get_words(self, words: List[str], maxWidth: int, i: int):
        line = []
        curr_len = 0

        # construct a line of words
        # consider the space between words
        while i < len(words) and curr_len + len(words[i]) <= maxWidth:
            line.append(words[i])
            curr_len += len(words[i]) + 1
            i += 1

        return line

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        n = len(words)
        res = []

        i = 0
        while i < n:
            # get line of words
            line = self.get_words(words, maxWidth, i)
            i += len(line)

            # evalute the length of line excluding the last space
            line_len = sum(len(w) + 1 for w in line) - 1
            # print("i: ", i, "line_len: ", line_len)

            # evalute the left space
            left_space = maxWidth - line_len
            # print("left space: ", left_space)

            # if line has only one word or it is the last line
            # then add spaces to the right
            if len(line) == 1 or i == len(words):
                res.append(" ".join(line) + " " * left_space)
                continue

            w_cnt = len(line) - 1
            # evaluate the space between words and extra space
            in_between_space = left_space // w_cnt
            extra_space = left_space % w_cnt

            # print(in_between_space, extra_space)

            # add spaces to the right of each word
            for j in range(extra_space):
                line[j] += " "

            # add spaces between words
            for j in range(w_cnt):
                line[j] += " " * in_between_space

            res.append(" ".join(line))

        return res


print(
    Solution().fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification."], 16
    )
)
print(
    Solution().fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16)
)
