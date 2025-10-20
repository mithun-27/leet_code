"""Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return the maximum possible value of k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1]

Output: 3

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7]

Output: 2

Explanation:

The subarray starting at index 0 is [1, 2], which is strictly increasing.
The subarray starting at index 2 is [3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 2 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist."""

#answer
class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        up, preUp, res = 1, 0, 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up += 1
            else:
                preUp = up
                up = 1
            half = up >> 1
            m = min(preUp, up)
            candidate = max(half, m)
            if candidate > res:
                res = candidate
        return res
    
#example
s = Solution()
print(s.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1])) # Output: 3
print(s.maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7])) # Output: 2 


"""walkthrough
1. The function maxIncreasingSubarrays is defined within the Solution class.
2. It takes one parameter: nums (a list of integers).
3. The function initializes variables to track the length of the current increasing subarray (up), the length of the previous increasing subarray (preUp), and the result (res).
4. It iterates through the nums array, updating the lengths of increasing subarrays as it goes.
5. For each element, it calculates the maximum possible k for adjacent increasing subarrays and updates the result if a larger k is found.
6. Finally, it returns the maximum value of k found.
"""