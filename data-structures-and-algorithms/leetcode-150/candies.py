from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # ratings = [1, 0, 2]
        # candies = [1, 1, 1]
        # Approach 1: Brute force
        # Approach 2: linear with 2 arrays
        # Approach 3: linear with array
        # Approach 4: linear with variables

        # changed = True

        # while changed:
        #     changed = False
        #     for i in range(n):
        #         if (i != n - 1
        #             and ratings[i] > ratings[i + 1]
        #             and candies[i] <= candies[i + 1]):

        #             candies[i] = candies[i + 1] + 1
        #             changed = True

        #         if (i > 0
        #             and ratings[i] > ratings[i - 1]
        #             and candies[i] <= candies[i - 1]):

        #             candies[i] = candies[i - 1] + 1
        #             changed = True

        # return sum(candies)

        # Approach 3: linear with array

        # initial candies
        candies = [1] * n

        # forward pass to distribute the candies if the current rating is increasing to the left
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # backward pass to distribute the candies if the current rating is increasing to the right
        # and candies are not already greater than the right
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # return the sum of the candies
        return sum(candies)


print(Solution().candy([1, 0, 2]))  # 5
print(Solution().candy([3, 2, 1]))  # 6
print(Solution().candy([1, 2, 3, 4, 5]))  # 15
print(Solution().candy([1, 3, 2, 2, 1]))  # 7
print(Solution().candy([1, 2, 87, 87, 87, 2, 1]))  # 13
print(Solution().candy([1, 3, 4, 5, 2]))  # 11
