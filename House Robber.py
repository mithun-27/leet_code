"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400"""

#answer
from git import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
#example usage
Solution().rob([1,2,3,1])  # Example call to the function
Solution().rob([2,7,9,3,1])  # Example call to the function
print(Solution().rob([2,1,1,2]))  # Example call to the function         4

"""walkthrough
1. We define a class Solution with a method rob that takes a list of integers nums as input.
2. We initialize two variables rob1 and rob2 to keep track of the maximum amount of money that can be robbed up to the previous two houses. 
3. We iterate through each house's amount of money in nums.
4. For each house, we calculate the maximum amount of money that can be robbed by either robbing the current house (num + rob1) or skipping it (rob2).  
5. We update rob1 to be the previous rob2 and rob2 to be the newly calculated maximum amount.
6. Finally, we return rob2, which contains the maximum amount of money that can be robbed without alerting the police.
"""