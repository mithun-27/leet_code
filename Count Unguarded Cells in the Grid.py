"""You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

 

Example 1:


Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
Example 2:


Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
 

Constraints:

1 <= m, n <= 105
2 <= m * n <= 105
1 <= guards.length, walls.length <= 5 * 104
2 <= guards.length + walls.length <= m * n
guards[i].length == walls[j].length == 2
0 <= rowi, rowj < m
0 <= coli, colj < n
All the positions in guards and walls are unique."""

#answer

from typing import List, Set, Tuple

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guards_set: Set[Tuple[int, int]] = {(r, c) for r, c in guards}
        walls_set: Set[Tuple[int, int]] = {(r, c) for r, c in walls}
        
        guarded = [[False] * n for _ in range(m)]
        
        # Row sweeps
        for r in range(m):
            # Left -> Right
            seen = False
            for c in range(n):
                if (r, c) in walls_set:
                    seen = False
                elif (r, c) in guards_set:
                    seen = True
                else:
                    if seen:
                        guarded[r][c] = True
            # Right -> Left
            seen = False
            for c in range(n - 1, -1, -1):
                if (r, c) in walls_set:
                    seen = False
                elif (r, c) in guards_set:
                    seen = True
                else:
                    if seen:
                        guarded[r][c] = True
        
        # Column sweeps
        for c in range(n):
            # Top -> Bottom
            seen = False
            for r in range(m):
                if (r, c) in walls_set:
                    seen = False
                elif (r, c) in guards_set:
                    seen = True
                else:
                    if seen:
                        guarded[r][c] = True
            # Bottom -> Top
            seen = False
            for r in range(m - 1, -1, -1):
                if (r, c) in walls_set:
                    seen = False
                elif (r, c) in guards_set:
                    seen = True
                else:
                    if seen:
                        guarded[r][c] = True
        
        # Count unguarded, unoccupied cells
        ans = 0
        for r in range(m):
            for c in range(n):
                if (r, c) not in walls_set and (r, c) not in guards_set and not guarded[r][c]:
                    ans += 1
        return ans


#example usage
sol = Solution()
print(sol.countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]))  # Output: 7
print(sol.countUnguarded(3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]]))  # Output: 4

"""Walkthrough
1. We first convert the lists of guards and walls into sets for O(1) lookup times.
2. We create a 2D list 'guarded' initialized to False to keep track of which cells are guarded.
3. We perform four sweeps (left to right, right to left, top to bottom, bottom to top) to mark the cells that are guarded by any guard.
4. Finally, we count the number of cells that are neither walls nor guards and are not marked as guarded.2. We create a dummy node to simplify edge cases where the head needs to be removed.
3. We iterate through the linked list using two pointers, prev and curr.
   - If the current node's value is in the remove set, we skip it by adjusting the prev pointer's next to curr's next.
   - If not, we move the prev pointer to curr.
4. We return the modified linked list starting from dummy.next."""