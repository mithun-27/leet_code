"""You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.

You then do the following steps:

If original is found in nums, multiply it by two (i.e., set original = 2 * original).
Otherwise, stop the process.
Repeat this process with the new number as long as you keep finding the number.
Return the final value of original.

 

Example 1:

Input: nums = [5,3,6,1,12], original = 3
Output: 24
Explanation: 
- 3 is found in nums. 3 is multiplied by 2 to obtain 6.
- 6 is found in nums. 6 is multiplied by 2 to obtain 12.
- 12 is found in nums. 12 is multiplied by 2 to obtain 24.
- 24 is not found in nums. Thus, 24 is returned.
Example 2:

Input: nums = [2,7,9], original = 4
Output: 4
Explanation:
- 4 is not found in nums. Thus, 4 is returned.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i], original <= 1000"""

#answer
from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)
        while original in s:
            original *= 2
        return original

#sample usage
sol = Solution()
print(sol.findFinalValue([5,3,6,1,12], 3))  # Output: 24
print(sol.findFinalValue([2,7,9], 4))  # Output: 4
print(sol.findFinalValue([1,2,4,8], 2))  # Output: 16

"""walkthrough
1. Convert the list `nums` into a set `s` for O(1) average time complexity lookups.
2. Use a while loop to check if `original` is in the set `s`.
3. If it is, multiply `original` by 2.
4. Repeat until `original` is not found in the set.
5. Return the final value of `original`.
6. This approach ensures efficient searching and updating of the `original` value.
"""