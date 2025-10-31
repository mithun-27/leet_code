"""You are given an integer array nums and two integers k and numOperations.

You must perform an operation numOperations times on nums, where in each operation you:

Select an index i that was not selected in any previous operations.
Add an integer in the range [-k, k] to nums[i].
Return the maximum possible frequency of any element in nums after performing the operations.

 

Example 1:

Input: nums = [1,4,5], k = 1, numOperations = 2

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1], after which nums becomes [1, 4, 5].
Adding -1 to nums[2], after which nums becomes [1, 4, 4].
Example 2:

Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1]."""

#answer

from bisect import bisect_right


class Solution:
    
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        
        arrayValMaxFreq = self.maxFrequencyOfArrayVal(nums, k , numOperations) 

        
        left = 0 
        otherValMaxFreq = 0
        for right in range(len(nums)):
            
            while nums[right] > nums[left] + 2*k:
                left += 1
            
            otherValMaxFreq = max(otherValMaxFreq, right - left + 1)
            
            if otherValMaxFreq >= numOperations:
                otherValMaxFreq = numOperations
                break
            
        return max(arrayValMaxFreq, otherValMaxFreq)


    
    def maxFrequencyOfArrayVal(self, nums, k, numOperations):
        
        count = Counter(nums)

        maxFreq = 0
        
        for val in count.keys():
            left = bisect_left(nums, val - k)
            right = bisect_right(nums, val + k) - 1
            freq = min(right - left + 1, numOperations + count[val])
            maxFreq = max(maxFreq, freq)

        return maxFreq

#example usage
s = Solution()
print(s.maxFrequency([1,4,5], 1, 2))  # Output: 2
print(s.maxFrequency([5,11,20,20], 5, 1))  # Output: 2

"""walkthrough
1. We define a class Solution with a method maxFrequency that takes an integer array nums, and two integers k and numOperations as input.
2. We sort the nums array to facilitate frequency calculations.
3. We define a helper method maxFrequencyOfArrayVal that calculates the maximum frequency of any element in nums after performing the operations.
4. In maxFrequencyOfArrayVal, we use a Counter to count the frequency of each number in nums.
5. We iterate through each unique value in nums and use binary search (bisect_left and bisect_right) to find the range of elements that can be changed to the current value within the allowed range [-k, k].
6. We calculate the maximum frequency possible for each value and update the overall maximum frequency.
7. In the main maxFrequency method, we also consider the case where we can change elements to values other than those in nums, by checking the range of values that can be achieved with the given k.
8. Finally, we return the maximum frequency obtained from both scenarios."""