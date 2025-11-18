"""You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.

Each power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station at city i can provide power to all cities j such that |i - j| <= r and 0 <= i, j <= n - 1.

Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.
The power of a city is the total number of power stations it is being provided power from.

The government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.

Given the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.

Note that you can build the k power stations in multiple cities.

 

Example 1:

Input: stations = [1,2,4,5,0], r = 1, k = 2
Output: 5
Explanation: 
One of the optimal ways is to install both the power stations at city 1. 
So stations will become [1,4,4,5,0].
- City 0 is provided by 1 + 4 = 5 power stations.
- City 1 is provided by 1 + 4 + 4 = 9 power stations.
- City 2 is provided by 4 + 4 + 5 = 13 power stations.
- City 3 is provided by 5 + 4 = 9 power stations.
- City 4 is provided by 5 + 0 = 5 power stations.
So the minimum power of a city is 5.
Since it is not possible to obtain a larger power, we return 5.
Example 2:

Input: stations = [4,4,4,4], r = 0, k = 3
Output: 4
Explanation: 
It can be proved that we cannot make the minimum power of a city greater than 4.
 

Constraints:

n == stations.length
1 <= n <= 105
0 <= stations[i] <= 105
0 <= r <= n - 1
0 <= k <= 109"""

#answer

from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        prefix = [0] * (n + 1)
        for i, x in enumerate(stations, 1):
            prefix[i] = prefix[i - 1] + x

        # Helper: sum of stations[l..r] (clamped to [0..n-1])
        def window_sum(i: int) -> int:
            L = max(0, i - r)
            R = min(n - 1, i + r)
            return prefix[R + 1] - prefix[L]

        # Binary search over answer
        low, high = 0, sum(stations) + k  # upper bound is safe
        # Precompute base power for i=0 window start
        base = window_sum(0)

        def feasible(x: int) -> bool:
            # Greedy: difference array for added stations' effect
            add_diff = [0] * (n + 1)  # we only touch indices up to n
            add_run = 0               # running sum of active added power at i
            k_left = k

            # We'll maintain base window sum as we sweep
            curr_base = base

            for i in range(n):
                # End any added effect scheduled here
                add_run += add_diff[i]

                curr_power = curr_base + add_run
                if curr_power < x:
                    need = x - curr_power
                    if need > k_left:
                        return False
                    k_left -= need

                    pos = min(n - 1, i + r)     # place new stations here
                    # They affect [pos - r, pos + r], which from our sweep POV starts at i
                    add_run += need
                    end = pos + r + 1
                    if end <= n:
                        add_diff[end] -= need

                # Move base window to next city: remove left-leaving, add right-entering
                if i < n - 1:
                    left_out = i - r
                    right_in = i + r + 1
                    if left_out >= 0:
                        curr_base -= stations[left_out]
                    if right_in < n:
                        curr_base += stations[right_in]

            return True

        # Binary search (upper mid)
        while low < high:
            mid = (low + high + 1) // 2
            if feasible(mid):
                low = mid
            else:
                high = mid - 1
        return low

#example usage
solution = Solution()
print(solution.maxPower([1,2,4,5,0], 1, 2))  # Output: 5
print(solution.maxPower([4,4,4,4], 0, 3))  # Output: 4
print(solution.maxPower([0,0,0,0], 2, 8))  # Output: 2


"""walkthrough of the code:
1. We define a function maxPower that takes in the list of stations, the range r, and the number of additional stations k.
2. We calculate the prefix sum of the stations to efficiently compute the power provided to each city.
3. We define a helper function window_sum to calculate the total power provided to a city considering the range r.
4. We perform a binary search to find the maximum possible minimum power of a city.
5. The feasible function checks if it's possible to achieve at least x power in every city by greedily placing additional stations where needed.
6. Finally, we return the maximum minimum power found through binary search."""