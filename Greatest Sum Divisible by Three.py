"""Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

Constraints:

1 <= nums.length <= 4 * 104
1 <= nums[i] <= 104"""

#answer
class Solution:
    def maxSumDivThree(self, nums):
        total = sum(nums)

        # store smallest two elements by remainder classes
        r1 = []
        r2 = []
        for x in nums:
            if x % 3 == 1:
                r1.append(x)
            elif x % 3 == 2:
                r2.append(x)

        r1.sort()
        r2.sort()

        mod = total % 3
        if mod == 0:
            return total

        # otherwise try removing minimal loss
        ans = 0
        if mod == 1:
            option1 = r1[0] if len(r1) >= 1 else float('inf')
            option2 = sum(r2[:2]) if len(r2) >= 2 else float('inf')
            ans = total - min(option1, option2)
        else:  # mod == 2
            option1 = r2[0] if len(r2) >= 1 else float('inf')
            option2 = sum(r1[:2]) if len(r1) >= 2 else float('inf')
            ans = total - min(option1, option2)

        return ans if ans != float('inf') else 0

#sample test case
solution = Solution()
print(solution.maxSumDivThree([3,6,5,1,8]))  # Output: 18
print(solution.maxSumDivThree([4]))          # Output: 0
print(solution.maxSumDivThree([1,2,3,4,4]))  # Output: 12