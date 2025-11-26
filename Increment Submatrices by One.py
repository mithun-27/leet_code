"""You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.

You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:

Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i.
Return the matrix mat after performing every query.

 

Example 1:


Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
Output: [[1,1,0],[1,2,1],[0,1,1]]
Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).
Example 2:


Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
Explanation: The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.
 

Constraints:

1 <= n <= 500
1 <= queries.length <= 104
0 <= row1i <= row2i < n
0 <= col1i <= col2i < n"""

#answer
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # Build final matrix via prefix sums
        for i in range(n):
            for j in range(1, n):
                diff[i][j] += diff[i][j - 1]

        for j in range(n):
            for i in range(1, n):
                diff[i][j] += diff[i - 1][j]

        # Remove extra row/col
        res = [row[:n] for row in diff[:n]]
        return res

#sample usage
Solution().rangeAddQueries(3, [[1,1,2,2],[0,0,1,1]])  # Expected output: [[1,1,0],[1,2,1],[0,1,1]]
Solution().rangeAddQueries(2, [[0,0,1,1]])              # Expected output: [[1,1],[1,1]]

"""walkthrough
1. We define a class Solution with a method rangeAddQueries that takes an integer n and a list of queries as input. 
2. We create a difference matrix diff of size (n+1) x (n+1) initialized to zero. This matrix will help us efficiently apply the range updates.
3. For each query, we update the corners of the submatrix in the difference matrix to reflect the addition of 1 to the specified submatrix.
4. After processing all queries, we compute the prefix sums for both rows and columns to build the final matrix.
5. Finally, we remove the extra row and column from the difference matrix to get the resulting n x n matrix and return it.
"""