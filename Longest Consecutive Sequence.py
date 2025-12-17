"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109"""

#answer
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
# Example usage:
solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2]))  # Output: 4
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # Output: 9
print(solution.longestConsecutive([1,0,1,2]))  # Output: 3

"""walkthrough
1. We define a class Solution with a method longestConsecutive that takes a list of integers nums as input.
2. We convert the nums list into a set called numSet to allow for O(1) average time complexity for lookups.
3. We initialize a variable longest to keep track of the length of the longest consecutive sequence found so far.
4. We iterate through each number in numSet. For each number, we check if it is the start of a sequence by verifying that (num - 1) is not in numSet.
5. If the number is the start of a sequence, we initialize a variable length to 1 and use a while loop to check for consecutive numbers (num + length) in numSet, incrementing length for each consecutive number found.
6. After finding the length of the current consecutive sequence, we update longest to be the maximum of its current value and the length of the current sequence.
7. Finally, we return the value of longest, which represents the length of the longest consecutive elements sequence in the input list.
"""