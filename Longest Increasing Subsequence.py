"""Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?"""

#answer
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue

            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]

        return LIS

#example usage
solution = Solution()   
print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))  # Output: 4
print(solution.lengthOfLIS([0,1,0,3,2,3]))  # Output: 4
print(solution.lengthOfLIS([7,7,7,7,7,7,7]))  # Output: 1   

"""walkthrough
1. Initialize an empty list dp to store the longest increasing subsequence found so far. Append the first element of nums to dp and set LIS (the length of the longest increasing subsequence) to 1.
2. Iterate through the nums array starting from the second element. For each element nums[i], compare it with the last element in dp. If nums[i] is greater than the last element in dp, it means we can extend the longest increasing subsequence, so we append nums[i] to dp and increment LIS by 1.      
3. If nums[i] is not greater than the last element in dp, we need to find the correct position in dp to replace an element with nums[i]. We use the bisect_left function from the bisect module to find the index idx where nums[i] should be inserted to maintain the sorted order of dp. We then replace the element at index idx in dp with nums[i]. This step ensures that we are always maintaining the longest increasing subsequence found so far.       
4. After iterating through all elements in nums, we return the value of LIS, which represents the length of the longest strictly increasing subsequence.    
5. The time complexity of this algorithm is O(n log(n)) due to the use of binary search (bisect_left) for finding the correct position in dp, and the space complexity is O(n) for storing the longest increasing subsequence in dp.        
6. The bisect_left function is used to find the insertion point for nums[i] in dp while maintaining the sorted order. If nums[i] is already present in dp, bisect_left will return the index of the first occurrence of nums[i], which allows us to replace it with the new value if necessary. This helps in maintaining the longest increasing subsequence efficiently.
"""