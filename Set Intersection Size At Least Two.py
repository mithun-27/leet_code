"""You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

A containing set is an array nums where each interval from intervals has at least two integers in nums.

For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
Return the minimum possible size of a containing set.

 

Example 1:

Input: intervals = [[1,3],[3,7],[8,9]]
Output: 5
Explanation: let nums = [2, 3, 4, 8, 9].
It can be shown that there cannot be any containing array of size 4.
Example 2:

Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3
Explanation: let nums = [2, 3, 4].
It can be shown that there cannot be any containing array of size 2.
Example 3:

Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
Output: 5
Explanation: let nums = [1, 2, 3, 4, 5].
It can be shown that there cannot be any containing array of size 4.
 

Constraints:

1 <= intervals.length <= 3000
intervals[i].length == 2
0 <= starti < endi <= 108"""

#answer

from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda iv: (iv[1], -iv[0]))
        
        ans = 0
       
        x = -10**18
        y = -10**18
        
        for L, R in intervals:
            if y < L:
                
                x = R - 1
                y = R
                ans += 2
            elif x < L <= y:
                
                x = y
                y = R
                ans += 1
            else:
                continue
        return ans

#sample usage
sol = Solution()
print(sol.intersectionSizeTwo([[1,3],[3,7],[8,9]]))  # Output: 5
print(sol.intersectionSizeTwo([[1,3],[1,4],[2,5],[3,5]]))  # Output: 3
print(sol.intersectionSizeTwo([[1,2],[2,3],[2,4],[4,5]]))  # Output: 5

"""walkthrough
1. Sort the intervals based on their end points. If two intervals have the same end point, sort by start point in descending order.
2. Initialize two variables `x` and `y` to track the last two points added to the containing set, and a counter `ans` to count the size of the containing set.
3. Iterate through each interval `[L, R]`:
    - If both `x` and `y` are less than `L`, it means neither of the last two points are in the current interval. Add two new points `R-1` and `R` to the containing set, update `x` and `y`, and increment `ans` by 2.
    - If only `x` is less than `L` but `y` is within the interval, add one new point `R` to the containing set, update `x` to be `y`, update `y` to be `R`, and increment `ans` by 1.
    - If both `x` and `y` are within the interval, do nothing as the interval already has at least two points in the containing set.
4. Return the total count `ans` which represents the minimum size of the containing set.
"""