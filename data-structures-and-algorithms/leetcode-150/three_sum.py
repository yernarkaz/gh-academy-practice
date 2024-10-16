import random
from typing import List
from tqdm import tqdm

random.seed(42)


class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds all unique pairs of integers in the given list that sum up to the target value.

        Args:
            nums (List[int]): A list of integers.
            target (int): The target sum for the pairs.

        Returns:
            List[int]: A list of unique pairs (tuples) of integers that sum up to the target value.
        """
        hmap = dict()
        res = set()

        for num in nums:
            complement = target - num

            if complement in hmap:
                res.add((complement, hmap[complement]))

            hmap[num] = complement

        return list(res)

    def twoSum2(self, nums: List[int], i: int, res: List[int]):
        """
        Finds all unique pairs in the list `nums` that sum up to zero when added to the element at index `i`.

        Args:
            nums (List[int]): The list of integers to search for pairs.
            i (int): The index of the current element to which pairs are being summed.
            res (List[int]): The list to store the resulting pairs that sum up to zero.

        Returns:
            None: The results are appended to the `res` list.
        """
        lo = i + 1
        hi = len(nums) - 1

        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if s < 0:
                lo += 1
            elif s > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1

                # avoid duplicates
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1

    def threeSum(self, nums: List[int], target: int) -> List[int]:
        # res = set()
        nums.sort()
        res = []

        for i in range(len(nums)):
            # if the current element is greater than zero, then the sum of the current element and the next two elements will be greater than zero
            if nums[i] > 0:
                break

            # avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            self.twoSum2(nums, i, res)
        # "x, y, z => x + y + z = target => target - x = y + z"
        # for i in range(len(nums) - 2):
        #     for two_sum_pairs in self.twoSum(nums[i + 1 :], target - nums[i]):
        #         res.add(tuple([nums[i]] + list(two_sum_pairs)))

        return res


# print("test case 1: ", Solution().twoSum([1, 2, 3, 4, 5, 6, 7], 12))
# print("test case 2:", Solution().twoSum([-1, 0, -1, 0, 1, 0], 0))

# print(
#     Solution().threeSum([1, 2, 3, 4, 5, 6, 7], 12)
# )  # [1,4,7], [1,5,6],[2,3,7], [2,4,6], [3,4,5], [3,4,5]
# print(Solution().threeSum([0, 1, 1], 0))  # []
# print(Solution().threeSum([0, 0, 0], 0))  # [0, 0, 0]
# print(Solution().threeSum([-1, 0, 1, 2, -1, -4], 0))  # [-1, -1, 2], [-1, 0, 1]
# print(Solution().threeSum([-1, 0, -1, 0, 1, 0], 0))  # [-1, 0, 1], [0, 0, 0]

# generate test case


n = 10000000
lo, hi = -(10**5), 10**5
len_min, len_max = 3, 10
test_cases = []
for _ in tqdm(range(n)):
    test_case = [
        random.randint(lo, hi) for _ in range(random.randint(len_min, len_max))
    ]
    test_cases.append(test_case)

results = []
for test_case in tqdm(test_cases):
    r = Solution().threeSum(test_case, 0)
    if len(r) > 0:
        results.append(r)

print("Number of three sums:", len(results))
# for r in results:
#     print(r)
#     print()
