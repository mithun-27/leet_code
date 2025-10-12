"""Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

Given an integer array rains where:

rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where:

ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.

 

Example 1:

Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.
Example 2:

Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
Example 3:

Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood."""

#answer
import bisect

class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        res = [1] * n
        last_rain = {}          
        dry_days = []           

        for day in range(n):
            r = rains[day]
            if r > 0:
                res[day] = -1
                if r in last_rain:
                    prev_day = last_rain[r]
                   
                    idx = bisect.bisect_right(dry_days, prev_day)
                    if idx == len(dry_days):
                        return []
                    dry_index = dry_days.pop(idx)
                    res[dry_index] = r
                last_rain[r] = day
            else:
                r
                bisect.insort(dry_days, day)

        return res

#example
solution = Solution()
print(solution.avoidFlood([1,2,3,4]))  # Output: [-1,-1,-1,-1]
print(solution.avoidFlood([1,2,0,0,2,1]))  # Output: [-1,-1,2,1,-1,-1]
print(solution.avoidFlood([1,2,0,1,2]))  # Output: []


"""walkthrough:
1. Import the bisect module to use binary search functions.
2. Define the Solution class with the avoidFlood method that takes the rains array as input.
3. Initialize variables:
   - n: Length of the rains array.
   - res: Result array initialized with 1s.
   - last_rain: Dictionary to track the last day each lake was filled.
   - dry_days: List to keep track of available dry days.
4. Iterate through each day in the rains array:
   - If it rains (r > 0):
     - Set res[day] to -1.
        - If the lake has been filled before (exists in last_rain):
        - Find the previous day it was filled.
        - Use bisect to find the first dry day after the previous fill day.
        - If no such dry day exists, return an empty array (flood is unavoidable).
        - Otherwise, pop that dry day from dry_days and set res[dry_index] to the lake number.
        - Update last_rain with the current day for the lake.
    - If it doesn't rain (r == 0):
        - Add the current day to dry_days.
        - Set res[day] to 1.
        - Use bisect.insort to maintain sorted order of dry_days.
5. Return the result array res after processing all days.
This approach ensures that we efficiently manage the drying of lakes to prevent floods while adhering to the constraints of the problem.
6. For each of the four possible directions (up, down, left, right), calculate the new cell coordinates (nx, ny). If the new cell is within bounds and has not been visited, mark it as visited and push it onto the heap with its elevation.
7. The process continues until we reach the target cell, ensuring that we always expand the least elevated cell first, which guarantees that we find the minimum time required to reach the destination.
"""