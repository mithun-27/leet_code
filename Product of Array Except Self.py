"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer."""

#answer
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


# Example usage:
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))  # Output: [24,12,8,6]
print(solution.productExceptSelf([-1,1,0,-3,3]))  # Output: [0,0,9,0,0]


"""walkthrough
1. We define a class Solution with a method productExceptSelf that takes a list of integers nums as input.  
2. We initialize a result list res with the same length as nums, filled with 1s. This list will eventually hold the final products.
3. We initialize a variable prefix to 1, which will be used to keep track of the product of all elements to the left of the current index.  
4. We iterate through the nums list from left to right. For each index i, we set res[i] to the current value of prefix (which represents the product of all elements to the left of i). Then, we update prefix by multiplying it with nums[i].  
5. We initialize a variable postfix to 1, which will be used to keep track of the product of all elements to the right of the current index.    
6. We iterate through the nums list from right to left. For each index i, we multiply res[i] by the current value of postfix (which represents the product of all elements to the right of i). Then, we update postfix by multiplying it with nums[i].  
7. Finally, we return the res list, which now contains the product of all elements except for the element at each index.
"""