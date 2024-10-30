from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Determines if the array contains any duplicates such that the two indices
        of the duplicate elements are at most `k` positions apart.

        Args:
            nums (List[int]): The list of integers to check for nearby duplicates.
            k (int): The maximum allowed distance between duplicate elements.

        Returns:
            bool: True if there are duplicates within `k` distance, False otherwise.
        """
        nums_dict = {}
        for i, num in enumerate(nums):
            if num in nums_dict and i - nums_dict[num] <= k:
                return True

            nums_dict[num] = i

        return False


# edge cases
assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 3) is True
assert Solution().containsNearbyDuplicate([1, 0, 1, 1], 1) is True
assert Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False
assert Solution().containsNearbyDuplicate([99, 99], 2) is True
assert Solution().containsNearbyDuplicate([99, 99], 3) is True

# tricky test cases
assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 0) is False
assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 1) is False
assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 2) is False
assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 3) is True
assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 4) is True
assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 5) is True

print("Passed all test cases!")
