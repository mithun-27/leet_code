"""Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer."""

#answer
from git import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        prefix = suffix = 0

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        return res
    
#exmaple usage
print(Solution().maxProduct([2,3,-2,4])) # Output: 6
print(Solution().maxProduct([-2,0,-1]))  # Output: 0
print(Solution().maxProduct([-2,3,-4]))  # Output: 24

"""walkthrough
1. Initialize variables:
   - n: Length of the input array nums.
   - res: Variable to store the maximum product found, initialized to the first element of nums.
   - prefix: Variable to store the product of the current prefix, initialized to 0. 
   - suffix: Variable to store the product of the current suffix, initialized to 0.
2. Loop through the array from 0 to n-1:
   - Update prefix by multiplying it with the current element nums[i]. If prefix is 0, use 1 instead to avoid resetting the product.
   - Update suffix by multiplying it with the current element from the end nums[n - 1 - i]. If suffix is 0, use 1 instead to avoid resetting the product.
   - Update res with the maximum of the current res, prefix, and suffix.    
3. After the loop, return res as the maximum product of a subarray.
The algorithm works by calculating the product of the prefix and suffix at each step, which allows it to handle negative numbers effectively. If a negative number is encountered, it can potentially turn a small product into a large one when multiplied with another negative number. By keeping track of both prefix and suffix products, we ensure that we consider all possible subarrays for the maximum product.       
4. The time complexity of this algorithm is O(n) since we traverse the array once, and the space complexity is O(1) as we are using only a constant amount of extra space.      
"""