"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000"""

#answer
class Solution:

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]),
                            self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
    
#example usage
Solution().rob([2,3,2])  # Example call to the function
Solution().rob([1,2,3,1])  # Example call to the function
print(Solution().rob([1,2,3]))  # Example call to the function
# Output: 3

"""walkthrough
1. We define a class Solution with a method rob that takes a list of integers nums as input.
2. Since the houses are arranged in a circle, we cannot rob both the first and last houses. Therefore, we consider two scenarios: robbing from the second house to the last house (nums[1:]) and robbing from the first house to the second-to-last house (nums[:-1]). We also consider the case where we only rob the first house (nums[0]).
3. We use a helper method to calculate the maximum amount of money that can be robbed for each of these scenarios.
4. The helper method uses a similar approach as in the linear house robber problem, maintaining two variables rob1 and rob2 to keep track of the maximum amounts that can be robbed up to the previous two houses. 
5. Finally, we return the maximum amount from the three scenarios.
"""