"""Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?"""

#answer
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
    
#example usage
solution = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
word2 = "SEE"
word3 = "ABCB"
print(solution.exist(board, word1))  # Output: True
print(solution.exist(board, word2))  # Output: True
print(solution.exist(board, word3))  # Output: False    

"""walkthrough
1. Define the exist method that takes a 2D board and a word as input.
2. Get the number of rows and columns in the board. 
3. Define a nested dfs function that performs depth-first search to find the word in the board.
4. In the dfs function, check if the current index i is equal to the length of the word. If so, return True.
5. Check if the current position (r, c) is out of bounds or if the character at board[r][c] does not match the current character in the word or if the cell has already been visited (marked as '#'). If any of these conditions are true, return False.
6. Mark the current cell as visited by setting board[r][c] to '#'.
7. Recursively call dfs for the four adjacent cells (down, up, right, left) and increment the index i by 1.
8. After exploring all four directions, restore the original character in board[r][c].
9. Iterate through each cell in the board and call the dfs function starting from that cell. If dfs returns True, return True from the exist method.
10. If no starting cell leads to finding the word, return False.
"""