"""You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

 

Example 1:

Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

Output: [6,10,12]

Explanation:

For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
Example 2:

Input: nums = [3,8,7,8,7,5], k = 2, x = 2

Output: [11,15,15,15,12]

Explanation:

Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

 

Constraints:

1 <= n == nums.length <= 50
1 <= nums[i] <= 50
1 <= x <= k <= nums.length"""

#answer

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if k == 0 or n == 0:
            return []
        
        # freq[v] = frequency of value v inside current window
        freq = defaultdict(int)

        # inBig: values currently selected among top-x
        inBig = set()

        # big: min-heap by (freq, value)  -> "worst" among selected is on top
        # store tuples (freq, value, val_id) where val_id == value (for clarity)
        big = []

        # small: max-heap by (freq, value), implemented via negatives
        # store tuples (-freq, -value, val_id)
        small = []

        # Sum over selected values: sum(freq[v] * v for v in inBig)
        sumBig = 0

        def push_value(v):
            """Push the current (freq[v], v) into the correct heap according to membership."""
            f = freq[v]
            if f == 0:
                return
            if v in inBig:
                heapq.heappush(big, (f, v, v))
            else:
                heapq.heappush(small, (-f, -v, v))

        def prune_big():
            """Remove stale entries from big (freq changed or membership changed)."""
            nonlocal big
            while big:
                f, v, _ = big[0]
                if freq[v] != f or v not in inBig or f == 0:
                    heapq.heappop(big)
                else:
                    break

        def prune_small():
            """Remove stale entries from small (freq changed or membership changed)."""
            nonlocal small
            while small:
                nf, nv, v = small[0]
                f, val = -nf, -nv
                if freq[v] != f or v in inBig or f == 0:
                    heapq.heappop(small)
                else:
                    break

        def promote():
            """Move the best candidate from small -> big (if any)."""
            nonlocal sumBig
            prune_small()
            if not small:
                return False
            nf, nv, v = heapq.heappop(small)
            f, val = -nf, -nv
            if freq[v] != f or f == 0 or v in inBig:
                return False  # stale; nothing to do (rebalance loop will try again)
            inBig.add(v)
            heapq.heappush(big, (f, val, v))
            sumBig += f * val
            return True

        def demote():
            """Move the worst selected from big -> small."""
            nonlocal sumBig
            prune_big()
            if not big:
                return False
            f, val, v = heapq.heappop(big)
            if freq[v] != f or v not in inBig or f == 0:
                return False  # stale; nothing to do
            inBig.remove(v)
            sumBig -= f * val
            heapq.heappush(small, (-f, -val, v))
            return True

        def rebalance():
            """Ensure: 
               1) |inBig| <= x
               2) |inBig| is as large as possible up to x
               3) all elements in big are >= any element in small by (freq, value)
            """
            # Fill up to x
            while len(inBig) < x:
                prune_small()
                if not small:
                    break
                if not promote():
                    break

            # If we have more than x, demote
            while len(inBig) > x:
                if not demote():
                    break

            # Fix ordering: if best of small beats worst of big, swap them
            while True:
                prune_big()
                prune_small()
                if not big or not small:
                    break
                f_big, val_big, v_big = big[0]    # worst in big
                f_sml, val_sml = -small[0][0], -small[0][1]  # best in small
                if (f_sml, val_sml) > (f_big, val_big):
                    # swap
                    demote()
                    promote()
                else:
                    break

        def add(v):
            """Add one occurrence of v to window."""
            nonlocal sumBig
            old = freq[v]
            freq[v] += 1
            
            if v in inBig:
                sumBig += v
            push_value(v)
            rebalance()

        def remove(v):
            """Remove one occurrence of v from window."""
            nonlocal sumBig
            if freq[v] == 0:
                return
            if v in inBig:
                sumBig -= v
            freq[v] -= 1
            push_value(v)  
            
            if freq[v] == 0 and v in inBig:
                
                inBig.remove(v)  
            rebalance()

        
        for i in range(k):
            add(nums[i])

        
        ans = [sumBig]
       
        for i in range(k, n):
            remove(nums[i - k])
            add(nums[i])
            ans.append(sumBig)

        return ans
    
#example usage
solution = Solution()
print(solution.findXSum([1,1,2,2,3,4,2,3], 6, 2)) # Output: [6,10,12]
print(solution.findXSum([3,8,7,8,7,5], 2, 2)) # Output: [11,15,15,15,12]
print(solution.findXSum([1,2,2,3,3,3,4,4,4,4], 5, 3)) # Output: [10,11,12,13,14,15]

"""walk through
1. Use two heaps (big and small) to maintain the top x frequent elements and the rest.
2. Use a frequency dictionary to track the count of each element in the current window.
3. For each sliding window, update the frequency counts, rebalance the heaps, and compute the x-sum.
4. Return the list of x-sums for each subarray of length k.
5. The rebalance function ensures that the heaps maintain the correct properties after each addition or removal of elements.
6. The promote and demote functions help in moving elements between the heaps based on their frequencies and values.
7. Add the minimum of curr_max_time and neededTime[i] to total_time.
4. Add the minimum of curr_max_time and neededTime[i] to total_time.
5. Update curr_max_time to be the maximum of curr_max_time and neededTime[i].
6. After the loop, return total_time which represents the minimum time needed to make the rope colorful.
6. After the loop, return total_time which represents the minimum time needed to make the rope colorful.
"""