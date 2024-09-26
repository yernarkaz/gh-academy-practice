from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        # [1,1,1,2,2,3] => [1,1,2,2,3]
        #

        # for i in range(1, n):
        #     if nums[i] == nums[i - 1]:
        #         curr_dup_cnt += 1
        #     else:
        #         curr_dup_cnt = 1

        #     if curr_dup_cnt <= 2:
        #         nums[j] = nums[i]
        #         j += 1

        j = 2
        for i in range(2, n):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j


nums = [1, 1, 1, 2, 2, 3]
sol = Solution()
k = sol.removeDuplicates(nums)
print(k)
print(nums[:k])
