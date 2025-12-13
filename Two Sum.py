"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

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
Only one valid answer exists."""


#answer

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pm={}
        for i , n in enumerate(nums):
            diff=target - n
            if diff in pm:
                return [pm[diff],i]
            pm[n]=i

# Example usage:
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))  # Output: [0, 1]
print(solution.twoSum([3,2,4], 6))      # Output: [1, 2]
print(solution.twoSum([3,3], 6))        # Output: [0, 1]

"""walkthrough
1. We define a class Solution with a method twoSum that takes a list of integers nums and an integer target as input.   
2. We initialize an empty dictionary pm to store the numbers we have seen so far along with their indices.
3. We iterate through the list nums using a for loop with enumerate to get both the index i and the number n at that index.
4. For each number n, we calculate the difference diff between the target and the current number n.
5. We check if this difference diff is already in the dictionary pm. If it is, it means we have found the two numbers that add up to the target, so we return their indices as a list: [pm[diff], i].
6. If the difference is not in the dictionary, we add the current number n and its index i to the dictionary pm.
7. We provide example usage of the Solution class to demonstrate how it works.
"""