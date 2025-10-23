"""You are given an integer array nums and an integer k.

You are allowed to perform the following operation on each element of the array at most once:

Add an integer in the range [-k, k] to the element.
Return the maximum possible number of distinct elements in nums after performing the operations.

 

Example 1:

Input: nums = [1,2,2,3,3,4], k = 2

Output: 6

Explanation:

nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

Example 2:

Input: nums = [4,4,4,4], k = 1

Output: 3

Explanation:

By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4]."""

#answer

from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        occupied = -10**30  

        for x in nums:
            
            if occupied < x + k:
                occupied = max(occupied + 1, x - k)
                ans += 1

        return ans


#example usage
s=Solution()
print(s.maxDistinctElements([1,2,2,3,3,4],2))  #Output: 6
print(s.maxDistinctElements([4,4,4,4],1))      #Output: 3
print(s.maxDistinctElements([1,1,1,1,1],0))  #Output: 1

"""walkthrough
1. Sort the input array nums to facilitate the process of finding distinct elements.
2. Initialize a variable ans to count the number of distinct elements and a variable occupied to keep track of the last occupied value.
3. Iterate through each element x in the sorted nums:
    - If the current occupied value is less than x + k, it means we can adjust x to create a new distinct element.
    - Update occupied to be the maximum of occupied + 1 (to ensure distinctness) and x - k (the lowest possible value after adjustment).
    - Increment the ans counter.
4. Return the total count of distinct elements stored in ans."""