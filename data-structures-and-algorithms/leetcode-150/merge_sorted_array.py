from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # 1,2,3,0,0,0
        # 2,5,6
        # 1,2,2,3,5,6

        # create a copy of nums1
        nums1_buf = nums1[:m].copy()
        i, j, k = 0, 0, 0

        while k < m + n:

            # k: 0, 1, 2, 3, 4, 5
            # i: 0, 1, 2, 2, 3, 3
            # j: 0, 0, 0, 1, 1, 2

            # 1<=2, 2<=2, 3>2, 3<=5, 5, 6

            # check if i exists in nums1_buf
            # otherwise populate nums1 with the remaining elements in nums2
            if n == 0 or (i < m and nums1_buf[i] <= nums2[j]):
                nums1[k] = nums1_buf[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

            k += 1


# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]
# m, n = 3, 3

# nums1 = [1]
# nums2 = []
# m, n = 1, 0

nums1 = [0]
nums2 = [1]
m, n = 0, 1

Solution().merge(nums1, m, nums2, n)
print(nums1)
