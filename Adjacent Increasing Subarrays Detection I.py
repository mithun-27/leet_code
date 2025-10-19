"""Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return true if it is possible to find two such subarrays, and false otherwise.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3

Output: true

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, so the result is true.
Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5

Output: false"""


#answer
class Solution:
    def hasIncreasingSubarrays(self, nums, k):
        n = len(nums)
        
        # Helper to check if a subarray is strictly increasing
        def is_increasing(start):
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        
        # Check adjacent subarrays
        for i in range(n - 2 * k + 1):
            if is_increasing(i) and is_increasing(i + k):
                return True
        
        return False
    
#example
s = Solution()
print(s.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3)) # Output: true
print(s.hasIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7], 5)) # Output: false


"""walkthrough
1. The function hasIncreasingSubarrays is defined within the Solution class.
2. It takes two parameters: nums (a list of integers) and k (an integer).
3. A helper function is_increasing is defined to check if a subarray of length k starting at a given index is strictly increasing.
4. The main function iterates through possible starting indices for adjacent subarrays of length k and checks if both are strictly increasing using the helper function.
5. If such adjacent subarrays are found, the function returns True; otherwise, it returns False after checking all possibilities.
"""