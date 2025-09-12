/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
*/
import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    
    public int[] twoSum(int[] nums, int target) {
        // Create a HashMap to store number as key and its index as value
        Map<Integer, Integer> map = new HashMap<>();
        
        // Loop through the array from index 0 to nums.length-1
        for (int i = 0; i < nums.length; i++) {
            // Calculate the complement that we need to find
    
        // complement + nums[i] = target, so complement = target - nums[i]
            int complement = target - nums[i];
            
            // Check if the complement exists in our HashMap
            // If it exists, it means we found our pair
            if (map.containsKey(complement)) {
                // Return the indices: first is the complement's index, second is current index
                return new int[]{map.get(complement), i};
            }
            
            // If complement doesn't exist, store current number and its index in HashMap
            // This number might be the complement for future elements
            map.put(nums[i], i);
        }
        
        // This line should never be reached according to problem constraints
        // Problem guarantees exactly one solution exists
        return new int[]{};
    }
    
    // Test method to verify our solution
    public static void main(String[] args) {
        TwoSum solution = new TwoSum();
        
        // Test case 1: nums = [2,7,11,15], target = 9
        // Expected output: [0,1] because nums[0] + nums[1] = 2 + 7 = 9
        int[] result1 = solution.twoSum(new int[]{2, 7, 11, 15}, 9);
        System.out.println("Test 1: [" + result1[0] + "," + result1[1] + "]");
        
        // Test case 2: nums = [3,2,4], target = 6  
        // Expected output: [1,2] because nums[1] + nums[2] = 2 + 4 = 6
        int[] result2 = solution.twoSum(new int[]{3, 2, 4}, 6);
        System.out.println("Test 2: [" + result2[0] + "," + result2[1] + "]");
        
        // Test case 3: nums = [3,3], target = 6
        // Expected output: [0,1] because nums[0] + nums[1] = 3 + 3 = 6
        int[] result3 = solution.twoSum(new int[]{3, 3}, 6);
        System.out.println("Test 3: [" + result3[0] + "," + result3[1] + "]");
    }
}













