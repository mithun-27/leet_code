"""There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104"""

#answer
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
    
#example usage
sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))  # Output: 4
print(sol.search([4,5,6,7,0,1,2], 3))  # Output: -1
print(sol.search([1], 0))  # Output: -1 

"""walkthrough
1. Initialize two pointers, `l` and `r`, to the start and end of the array.
2. While `l` is less than or equal to `r`, do the following:    
    a. Calculate the middle index `mid`.
    b. If the middle element `nums[mid]` is equal to the target, return `mid`.
    c. Determine which half of the array is sorted:
        - If the left half (`nums[l]` to `nums[mid]`) is sorted:
          i. Check if the target is within this range. If it is, adjust `r` to `mid - 1`. Otherwise, adjust `l` to `mid + 1`.
        - If the right half (`nums[mid]` to `nums[r]`) is sorted:
          i. Check if the target is within this range. If it is, adjust `l` to `mid + 1`. Otherwise, adjust `r` to `mid - 1`.
3. If the target is not found, return -1.
"""