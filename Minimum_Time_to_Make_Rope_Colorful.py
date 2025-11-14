"""Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

 

Example 1:


Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.
Example 2:


Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.
Example 3:


Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
 

Constraints:

n == colors.length == neededTime.length
1 <= n <= 105
1 <= neededTime[i] <= 104
colors contains only lowercase English letters."""

#answer

class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total_time, curr_max_time = 0, 0

        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                curr_max_time = 0
            total_time += min(curr_max_time, neededTime[i])
            curr_max_time = max(curr_max_time, neededTime[i])

        return total_time

#example usage
solution = Solution()
print(solution.minCost("abaac", [1,2,3,4,5])) # Output: 3
print(solution.minCost("abc", [1,2,3])) # Output: 0
print(solution.minCost("aabaa", [1,2,3,4,1])) # Output: 2

"""walk through
1. Initialize total_time and curr_max_time to 0.
2. Loop through each balloon in the colors string.
3. If the current balloon color is different from the previous one, reset curr_max_time to 0.
4. Add the minimum of curr_max_time and neededTime[i] to total_time. This accounts for the time needed to remove balloons.
5. Update curr_max_time to be the maximum of itself and neededTime[i].
6. After the loop, return total_time which represents the minimum time needed to make the rope colorful.
from typing import List, Set, Tuple 
"""