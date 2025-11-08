"""You are given an integer array nums.

Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either left or right.

After that, you repeat the following process:

If curr is out of the range [0, n - 1], this process ends.
If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, or decrementing curr if you are moving left.
Else if nums[curr] > 0:
Decrement nums[curr] by 1.
Reverse your movement direction (left becomes right and vice versa).
Take a step in your new direction.
A selection of the initial position curr and movement direction is considered valid if every element in nums becomes 0 by the end of the process.

Return the number of possible valid selections.

 

Example 1:

Input: nums = [1,0,2,0,3]

Output: 2

Explanation:

The only possible valid selections are the following:

Choose curr = 3, and a movement direction to the left.
[1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,1,0,3] -> [1,0,1,0,3] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,0,0,2] -> [1,0,0,0,2] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,0].
Choose curr = 3, and a movement direction to the right.
[1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,2,0,2] -> [1,0,2,0,2] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,1,0,1] -> [1,0,1,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [0,0,0,0,0].
Example 2:

Input: nums = [2,3,4,0,4,1,0]

Output: 0

Explanation:

There are no possible valid selections."""

#answer
class Solution:
    def countValidSelections(self, nums):
        total = sum(nums)
        prefix = 0
        ans = 0
        
        for x in nums:
            if x == 0:
                left = prefix
                right = total - prefix
                if left == right:
                    ans += 2
                elif abs(left - right) == 1:
                    ans += 1
            prefix += x
        
        return ans

#example usage
sol = Solution()
print(sol.countValidSelections([1,0,2,0,3]))  # Output: 2
print(sol.countValidSelections([2,3,4,0,4,1,0]))  # Output: 0

"""Walkthrough of the code:
1. We define a class Solution with a method countValidSelections that takes an integer array nums as input.
2. We calculate the total sum of the elements in nums and store it in the variable total
3. We initialize two variables: prefix to keep track of the sum of elements to the left of the current position, and ans to count the number of valid selections.
4. We iterate through each element x in nums:
   - If x is 0, we check the sums of the left and right sides of the current position.
   - We calculate left as the sum of elements to the left (prefix) and right as the sum of elements to the right (total - prefix).
   - If left equals right, it means we can select this position with both left and right directions, so we increment ans by 2.
   - If the absolute difference between left and right is 1, it means we can select this position with only one direction, so we increment ans by 1.
5. We update prefix by adding the current element x to it.
6. Finally, we return ans, which contains the total number of valid selections.
"""