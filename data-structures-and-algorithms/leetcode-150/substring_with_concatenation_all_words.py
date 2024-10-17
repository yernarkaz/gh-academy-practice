from typing import List
from collections import Counter


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []

        # Get the length of the words given in the list
        word_len = len(words[0])

        # Count the frequency of each word
        word_counter = Counter(words)

        # Iterate through word_len times
        for i in range(word_len):

            # Initialize two pointers
            start = i
            end = i

            # Initialize a counter to keep track of the frequency of the words in the substring
            current_counter = Counter()

            while end + word_len <= len(s):
                current_word = s[end : end + word_len]
                end += word_len
                current_counter[current_word] += 1

                # If the current word is not in the word counter, we reset the counter
                if current_word not in word_counter:
                    current_counter.clear()
                    start = end
                    continue

                # If the current word is in the word counter
                # but the frequency of the current word is greater than the frequency of the word in the word counter,
                # we remove the word from the start of the substring
                while current_counter[current_word] > word_counter[current_word]:
                    current_counter[s[start : start + word_len]] -= 1
                    start += word_len

                # If the current counter is equal to the word counter,
                # we add the start index to the result
                if current_counter == word_counter:
                    res.append(start)

        return res


assert Solution().findSubstring("a", ["a"]) == [0]
assert Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
assert (
    Solution().findSubstring(
        "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]
    )
    == []
)
# print(Solution().findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
assert Solution().findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]) == [
    6,
    9,
    12,
]
assert Solution().findSubstring(
    "wordgoodgoodgoodbestword", ["word", "good", "best", "good"]
) == [8]
assert Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
assert (
    Solution().findSubstring(
        "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]
    )
    == []
)
assert Solution().findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]) == [
    6,
    9,
    12,
]

assert Solution().findSubstring("ababaab", ["ab", "ba", "ba"]) == [1]
print("Passed all tests!")
