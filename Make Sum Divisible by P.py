"""Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

 

Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= p <= 109"""

#answer

from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        need = total % p
        if need == 0:
            return 0

        prefix = 0
        seen = {0: -1}  
        ans = len(nums)

        for i, x in enumerate(nums):
            prefix = (prefix + x) % p
            target = (prefix - need) % p

            if target in seen:
                ans = min(ans, i - seen[target])

            seen[prefix] = i

        return ans if ans < len(nums) else -1


# Example usage:solution = Solution()
print(solution.minSubarray([3,1,4,2], 6))  # Output: 1
print(solution.minSubarray([6,3,5,2], 9))  # Output: 2
print(solution.minSubarray([1,2,3], 3))    # Output: 0


"""walkthrough of the code:
1. We start by calculating the total sum of the array and determine the remainder when divided by p (need).
2. If need is 0, it means the total sum is already divisible by p, so we return 0.
3. We initialize a prefix sum variable and a dictionary (seen) to store the earliest index where each prefix sum modulo p occurs.
4. We iterate through the array, updating the prefix sum and calculating the target prefix sum that we need to find in order to form a subarray whose sum modulo p equals need.
5. If the target prefix sum exists in the seen dictionary, we calculate the length of the subarray and update the answer if it's smaller than the previously recorded answer.
6. Finally, we return the length of the smallest subarray found, or -1 if no valid subarray exists."""