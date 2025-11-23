"""You are given a 0-indexed array nums consisting of positive integers. You can do the following operation on the array any number of times:

Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

The gcd of two integers is the greatest common divisor of the two integers.

 

Example 1:

Input: nums = [2,6,3,4]
Output: 4
Explanation: We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
Example 2:

Input: nums = [2,10,6,14]
Output: -1
Explanation: It can be shown that it is impossible to make all the elements equal to 1.
 

Constraints:

2 <= nums.length <= 50
1 <= nums[i] <= 106"""

#answer
from typing import List
import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones > 0:
            return n - ones

        
        INF = 10**9
        min_len_minus1 = INF  
        for i in range(n):
            g = nums[i]
            if g == 1:
                min_len_minus1 = 0
                break
            for j in range(i+1, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_len_minus1 = min(min_len_minus1, j - i)
                    break  

        if min_len_minus1 == INF:
            return -1

        
        return min_len_minus1 + (n - 1)

# Example usage:
solution = Solution()
print(solution.minOperations([2,6,3,4]))  # Output: 4
print(solution.minOperations([2,10,6,14]))  # Output: -1
print(solution.minOperations([4,3,2,1]))  # output: 3