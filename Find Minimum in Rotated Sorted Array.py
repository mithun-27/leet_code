"""Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times."""

#answer
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
    
#example usage
sol = Solution()
print(sol.findMin([3,4,5,1,2]))  # Output: 1
print(sol.findMin([4,5,6,7,0,1,2]))  # Output: 0
print(sol.findMin([11,13,15,17]))  # Output: 11 

"""walkthrough
1. Initialize two pointers, `l` and `r`, to the start and end of the array.
2. While `l` is less than `r`, do the following:
   a. Calculate the middle index `m`.
   b. If the middle element `nums[m]` is less than the rightmost element `nums[r]`, it means the minimum element is in the left half (including `m`), so update `r` to `m`.
   c. Otherwise, the minimum element is in the right half (excluding `m`), so update `l` to `m + 1`.
3. When the loop ends, `l` will point to the minimum element in the array. Return `nums[l]`.
4. This algorithm runs in O(log n) time due to the binary search approach.
5. The space complexity is O(1) since we are using only a constant amount of extra space.
6. Test the function with example inputs to verify correctness.
        m = l + (r - l) // 2
7. Expand the right pointer `r` to include more characters from `s`.
    - Update the frequency of the character at `s[r]` in the `window` dictionary.
    - If the frequency of this character in the `window` matches its frequency in `countT`, increment `have`.
8. While `have` equals `need`, it means the current window contains all characters from `t`:
    - Check if the current window size is smaller than the previously recorded minimum window size. If
      it is, update `res` and `resLen`.
    - Shrink the window from the left by moving the `l` pointer to the right.
    - Decrement the frequency of the character at `s[l]` in the `window` dictionary.
    - If this character is in `countT` and its frequency in `window` drops below that in `countT`, decrement `have`.
9. After processing the entire string `s`, extract the substring using the indices stored in `res`. If no valid window was found, return an empty string.
"""