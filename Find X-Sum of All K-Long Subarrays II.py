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

nums.length == n
1 <= n <= 105
1 <= nums[i] <= 109
1 <= x <= k <= nums.length"""

#answer

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if k == 0 or n == 0:
            return []
        
        # freq[v] = frequency of value v in the current window
        freq = defaultdict(int)

        # inBig = set of values currently in the "selected" top-x set
        inBig = set()

        # big: min-heap of (freq, value, key) for the selected set (top-x)
        #      the "worst" among selected sits at the top
        big = []

        # small: max-heap of (-freq, -value, key) for the rest
        small = []

        # maintain sum over selected: sum(freq[v] * v for v in inBig)
        sumBig = 0

        def push_state(v):
            """Push current (freq[v], v) to the appropriate heap (lazy)."""
            f = freq[v]
            if f == 0:
                return
            if v in inBig:
                heapq.heappush(big, (f, v, v))
            else:
                heapq.heappush(small, (-f, -v, v))

        def prune_big():
            """Remove stale entries from big."""
            while big:
                f, val, v = big[0]
                if v not in inBig or freq[v] != f or f == 0:
                    heapq.heappop(big)
                else:
                    break

        def prune_small():
            """Remove stale entries from small."""
            while small:
                nf, nv, v = small[0]
                f, val = -nf, -nv
                if v in inBig or freq[v] != f or f == 0:
                    heapq.heappop(small)
                else:
                    break

        def promote_one():
            """Move the best candidate from small -> big."""
            nonlocal sumBig
            prune_small()
            if not small:
                return False
            nf, nv, v = heapq.heappop(small)
            f, val = -nf, -nv
            # validate
            if freq[v] != f or f == 0 or v in inBig:
                return False
            inBig.add(v)
            heapq.heappush(big, (f, val, v))
            sumBig += f * val
            return True

        def demote_one():
            """Move the worst selected from big -> small."""
            nonlocal sumBig
            prune_big()
            if not big:
                return False
            f, val, v = heapq.heappop(big)
            if v not in inBig or freq[v] != f or f == 0:
                return False
            inBig.remove(v)
            sumBig -= f * val
            heapq.heappush(small, (-f, -val, v))
            return True

        def rebalance():
            """Ensure big holds exactly the top-x (by (freq, value)) among values with freq>0."""
            # Fill up to x
            while len(inBig) < x:
                prune_small()
                if not small:
                    break
                if not promote_one():
                    break

            # Shrink if too many
            while len(inBig) > x:
                if not demote_one():
                    break

            # Fix boundary: best of small should not beat worst of big
            while True:
                prune_big()
                prune_small()
                if not big or not small:
                    break
                f_big, val_big, v_big = big[0]          # worst in big
                f_sml, val_sml = -small[0][0], -small[0][1]  # best in small
                if (f_sml, val_sml) > (f_big, val_big):
                    demote_one()
                    promote_one()
                else:
                    break

        def add(v):
            """Add one occurrence of v into window."""
            nonlocal sumBig
            was_in = v in inBig
            oldf = freq[v]
            freq[v] = oldf + 1
            if was_in:
                # contribution increases by +v
                sumBig += v
            push_state(v)
            rebalance()

        def remove(v):
            """Remove one occurrence of v from window."""
            nonlocal sumBig
            if freq[v] == 0:
                return
            was_in = v in inBig
            # contribution decreases by -v if it was selected
            if was_in:
                sumBig -= v
            freq[v] -= 1
            # If frequency dropped to 0 and it was selected, remove from inBig now.
            if freq[v] == 0 and was_in:
                inBig.remove(v)
            push_state(v)  # push new state lazily
            rebalance()

        # Build first window
        for i in range(k):
            add(nums[i])

        ans = [sumBig]

        # Slide
        for i in range(k, n):
            remove(nums[i - k])
            add(nums[i])
            ans.append(sumBig)

        return ans

# Example usage:
sol = Solution()
print(sol.findXSum([1,1,2,2,3,4,2,3], 6, 2))  # Output: [6,10,12]
print(sol.findXSum([3,8,7,8,7,5], 2, 2))    # Output: [11,15,15,15,12]
print(sol.findXSum([1,2,2,3,3,3,4,4,4,4], 5, 3))  # Output: [10,11,12,13,14,15]

"""walkthrough
1. Initialize frequency dictionary, two heaps (big and small), and a set to track elements in the top-x set.
2. Define helper functions to manage heaps, promote/demote elements, and rebalance the heaps.
3. Use sliding window technique to add/remove elements and maintain the x-sum for each subarray.
4. Return the list of x-sums for all k-length subarrays.
"""