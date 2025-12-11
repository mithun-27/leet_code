"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109"""


#answer

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Example usage:
solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))  # Output: True
print(solution.containsDuplicate([1,2,3,4]))  # Output: False
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # Output: True

"""walkthrough
1. We define a class Solution with a method containsDuplicate that takes a list of integers nums as input.
2. We initialize an empty set seen to keep track of the numbers we have encountered so far.
3. We iterate through each number num in the input list nums.   
4. For each number, we check if it is already in the seen set. If it is, we return True immediately, indicating that a duplicate has been found.
5. If the number is not in the seen set, we add it to the set.
6. If we finish iterating through the list without finding any duplicates, we return False, indicating that all elements are distinct.
"""