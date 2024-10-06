package assignments;

import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public static void main(String[] args) {
        testTwoSum(new int[]{2,-1,0,1,2,3,4}, 0, new int[]{1, -1});
        testTwoSum(new int[]{2, 7, 11, 15}, 9, new int[]{7, 2});
        testTwoSum(new int[]{3, 2, 4}, 6, new int[]{4, 2});
        testTwoSum(new int[]{3, 3}, 6, new int[]{3, 3});
    }

    public static void testTwoSum(int[] nums, int target, int[] expected) {
        int[] result = TwoSumHashmap(nums, target);
        System.out.println("Result: " + Arrays.toString(result));
        System.out.println("Expected: " + Arrays.toString(expected));
        System.out.println(Arrays.equals(result, expected) ? "Test passed" : "Test failed");
        System.out.println();
    }

    public static int[] TwoSumHashmap(int[] nums, int target) {
        int[] result = new int[2];
        HashMap<Integer, Integer> cache = new HashMap<>();
        /* x + y = target => y = target - x 
            -2: 2, 1:-1, 0:0
        */
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            if (cache.containsKey(nums[i])) {
                return new int[]{nums[i], complement};
            }

            cache.put(complement, nums[i]);
        }

        return result;
    }
}