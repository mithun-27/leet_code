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