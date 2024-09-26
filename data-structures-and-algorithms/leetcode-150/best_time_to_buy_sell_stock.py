from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left, right = 0, 1

        while right < len(prices) and left <= right:

            while right < len(prices) and prices[right] >= prices[left]:
                if prices[right] - prices[left] > profit:
                    profit = prices[right] - prices[left]

                right += 1

            left += 1

        return profit


print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([7, 6, 4, 10, 1]))
