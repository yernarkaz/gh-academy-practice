from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix_product, suffix_product = 1, 1
        n = len(nums)

        l, r = [1] * n, [1] * n
        for i in range(1, n):
            l[i] = l[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]

        res = []
        for i in range(n):
            res.append(l[i] * r[i])

        return res


print(Solution().productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
