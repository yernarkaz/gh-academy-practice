from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # net change in the amount of gas in the tank
        # when moving from station i to i + 1 is gas[i] - cost[i]

        # get starting index as the minimum cost to travel
        # start traveling and check if you can reach the starting index

        # gas=[1,2,3,4,5] cost=[3,4,5,1,2]

        # return -1 if total number of gas is less than total number of cost
        if sum(gas) < sum(cost):
            return -1

        # initialize total_gain and start_ind
        total_gain = 0
        start_ind = 0

        for i in range(len(gas)):
            # calculate total gain
            total_gain += gas[i] - cost[i]

            # if total gain is less than 0, then we need to start from the next station
            if total_gain < 0:
                start_ind = i + 1
                total_gain = 0

        # return starting index if total gain is greater than or equal to 0
        return start_ind if total_gain >= 0 else -1


print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # 3
print(Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]))  # -1
print(Solution().canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]))  # 4
