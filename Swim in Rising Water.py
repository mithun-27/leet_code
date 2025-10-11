"""You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

It starts raining, and water gradually rises over time. At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.

You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the minimum time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

Example 1:


Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:


Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected."""

#answer
import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        visited = set()
        min_heap = [(grid[0][0], 0, 0)]  # (elevation, x, y)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        res = 0
        
        while min_heap:
            elevation, x, y = heapq.heappop(min_heap)
            res = max(res, elevation)
            
            if (x, y) == (n-1, n-1):
                return res
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(min_heap, (grid[nx][ny], nx, ny))

#example
solution = Solution()
print(solution.swimInWater([[0,2],[1,3]]))  # Output: 3
print(solution.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))  # Output: 16
print(solution.swimInWater([[10,12,14],[9,11,13],[8,7,6]]))  # Output: 14
print(solution.swimInWater([[0]]))  # Output: 0


"""walkthrough:
To solve the problem of finding the minimum time until you can reach the bottom right square in a grid where each cell represents elevation, we can use a priority queue (min-heap) to implement a modified Dijkstra's algorithm. The idea is to always expand the least elevated cell that we can reach, ensuring that we are always considering the lowest possible water level at each step.
Here's a step-by-step breakdown of the approach:
1. Initialize a min-heap (priority queue) and add the starting cell (0, 0) with its elevation. Also, maintain a set to keep track of visited cells to avoid processing the same cell multiple times.
2. Define the possible directions for movement (up, down, left, right).
3. While the min-heap is not empty, do the following:
   a. Pop the cell with the lowest elevation from the heap.
   b. Update the result (res) to be the maximum of the current result and the elevation of the popped cell. This ensures that we are keeping track of the highest elevation we have encountered on our path.
   c. If we reach the bottom right cell (n-1, n-1), return the result as it represents the minimum time required to reach that cell.
   d. For each of the four possible directions, calculate the new cell coordinates (nx, ny). If the new cell is within bounds and has not been visited, mark it as visited and push it onto the heap with its elevation.
4. The process continues until we reach the target cell, ensuring that we always expand the least elevated cell first, which guarantees that we find the minimum time required to reach the destination.
This approach efficiently finds the minimum time to reach the bottom right cell by leveraging the properties of a priority queue and ensuring that we always consider the lowest elevation paths first."""
