"""There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans."""


#answer
class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        
        rows = len(heights)
        cols = len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c, ocean):
            ocean[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    not ocean[nr][nc] and 
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, ocean)
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        
        
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)
        
        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])
        
        return result
    
#example
solution = Solution()
print(solution.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))  # Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
print(solution.pacificAtlantic([[1]]))  # Output: [[0,0]]


"""walkthrough:
1. We define the `pacificAtlantic` method that takes a 2D list `heights` as input.
2. We check if the input is empty and return an empty list if it is.
3. We initialize the number of rows and columns, and create two 2D lists `pacific` and `atlantic` to track cells that can reach each ocean.
4. We define the `dfs` function that performs a depth-first search to mark reachable cells for a given ocean.
5. We perform DFS from the borders of the grid that touch the Pacific and Atlantic oceans.
6. Finally, we iterate through the grid to find cells that can reach both oceans and return the result.
"""