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

Adding 0 to nums[1]. nums becomes [1, 4, 5].
Adding -1 to nums[2]. nums becomes [1, 4, 4].
Example 2:

Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1].
 """

#answer

from collections import Counter

class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        """
        Find maximum frequency after performing at most numOperations operations.
        Each operation allows increasing or decreasing an element by at most k.
        
        Optimized approach using sweep line:
        - For each unique value as target, count how many can reach it
        - Use events to efficiently count overlapping ranges
        """
        freq = Counter(nums)
        

        events = []
        
        for num in nums:
           
            events.append((num - k, 1))      
            events.append((num + k + 1, -1))  
        
      
        events.sort()
        
        unique_vals = sorted(freq.keys())
        
        max_freq = 0
        current_reachable = 0
        event_idx = 0
        
        
        for target in unique_vals:
            
            while event_idx < len(events) and events[event_idx][0] <= target:
                current_reachable += events[event_idx][1]
                event_idx += 1
            
            
            already_equal = freq[target]
            
           
            can_change = current_reachable - already_equal
            
            
            total = already_equal + min(can_change, numOperations)
            max_freq = max(max_freq, total)
        
        
        all_positions = sorted(set(pos for pos, _ in events))
        current_reachable = 0
        event_idx = 0
        
        for pos in all_positions:
           
            while event_idx < len(events) and events[event_idx][0] <= pos:
                current_reachable += events[event_idx][1]
                event_idx += 1

            if pos not in freq:
                total = min(current_reachable, numOperations)
                max_freq = max(max_freq, total)
        
        return max_freq
    
#answer
s=solution = Solution()
print(s.maxFrequency([1,4,5], 1, 2))  # Output: 2
print(s.maxFrequency([5,11,20,20], 5, 1))  # Output: 2

"""walkthrough
1. We define a class Solution with a method maxFrequency that takes an integer array nums, and two integers k and numOperations as input.
2. We use a Counter to count the frequency of each number in nums.
3. We create a list of events to represent the ranges of values that can reach each number in nums by adding or subtracting up to k.
4. We sort the events and unique values in nums.
5. We iterate through each unique value as a target and use a sweep line technique to count
   how many numbers can reach that target.
6. For each target, we calculate the total frequency by adding the already equal numbers and the minimum of
   the numbers that can change and numOperations.
7. We also handle the case for positions that are not in the original nums array.
8. Finally, we return the maximum frequency found after processing all targets and positions.
"""