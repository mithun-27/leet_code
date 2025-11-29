"""Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

 

Example 1:


Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
Example 2:


Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
 

Constraints:

1 <= nums.length <= 105
0 <= k <= nums.length
nums[i] is 0 or 1"""

#answer
from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -float('inf')  # index of last seen 1; start far left
        for i, v in enumerate(nums):
            if v == 1:
                if i - prev - 1 < k:
                    return False
                prev = i
        return True

#sample usage
sol = Solution()
print(sol.kLengthApart([1,0,0,0,1,0,0,1], 2))  # Output: True
print(sol.kLengthApart([1,0,0,1,0,1], 2))      # Output: False
print(sol.kLengthApart([1,0,1,0,0,0,1], 2))  # Output: True

"""walkthrough
1. Initialize a variable `prev` to keep track of the index of the last seen '1'. Start it at negative infinity to handle the first '1' correctly.
2. Iterate through the list `nums` using `enumerate` to get both the index `i` and the value `v`.
3. For each element, check if `v` is '1':
   - If it is, check the distance from the last seen '1' (i.e., `i - prev - 1`).
   - If this distance is less than `k`, return `False` immediately.
   - Update `prev` to the current index `i`.    
4. If the loop completes without finding any violations, return `True`.
5. This approach ensures that we efficiently check the distance between consecutive '1's in a single pass through the list.
"""