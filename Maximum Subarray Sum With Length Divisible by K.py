"""You are given an array of integers nums and an integer k.

Return the maximum sum of a subarray of nums, such that the size of the subarray is divisible by k.

 

Example 1:

Input: nums = [1,2], k = 1

Output: 3

Explanation:

The subarray [1, 2] with sum 3 has length equal to 2 which is divisible by 1.

Example 2:

Input: nums = [-1,-2,-3,-4,-5], k = 4

Output: -10

Explanation:

The maximum sum subarray is [-1, -2, -3, -4] which has length equal to 4 which is divisible by 4.

Example 3:

Input: nums = [-5,1,2,-3,4], k = 2

Output: 4

Explanation:

The maximum sum subarray is [1, 2, -3, 4] which has length equal to 4 which is divisible by 2.

 

Constraints:

1 <= k <= nums.length <= 2 * 105
-109 <= nums[i] <= 109"""

#answer
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        INF = 10**30
        minPrefix = [INF] * k
        minPrefix[0] = 0

        prefix = 0
        answer = -10**30

        for i, x in enumerate(nums):
            prefix += x
            mod = (i + 1) % k

            if minPrefix[mod] != INF:
                answer = max(answer, prefix - minPrefix[mod])

            minPrefix[mod] = min(minPrefix[mod], prefix)

        return answer

#sample test case
solution = Solution()
print(solution.maxSubarraySum([1,2], 1))  # Output: 3
print(solution.maxSubarraySum([-1,-2,-3,-4,-5], 4))  # Output: -10
print(solution.maxSubarraySum([-5,1,2,-3,4], 2))  # Output: 4

"""walkthrough
1. Initialize a list `minPrefix` of size `k` with all values set to infinity, except for `minPrefix[0]` which is set to 0. This list will keep track of the minimum prefix sums for each modulo class.
2. Initialize a variable `prefix` to keep track of the current prefix sum and a variable `answer` to store the maximum subarray sum found, initialized to a very small number.  
3. Loop through each element `x` in the input list `nums`, along with its index `i`:
    a. Update the `prefix` sum by adding the current element `x`.
    b. Calculate the modulo `mod` of the current index + 1 with `k`.
    c. If there is a valid minimum prefix sum for this modulo class (i.e., `minPrefix[mod]` is not infinity), update the `answer` with the maximum of its current value and the difference between the current `prefix` and the minimum prefix sum for this modulo class.
    d. Update the minimum prefix sum for this modulo class with the current `prefix` if it is smaller than the existing value.
4. After processing all elements, return the `answer` which contains the maximum subarray sum with length divisible by `k`.
"""