"""There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100"""

#answer
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        if m < n:
            m, n = n, m

        res = j = 1
        for i in range(m, m + n - 1):
            res *= i
            res //= j
            j += 1

        return res
    
#example usage
solution = Solution()   
print(solution.uniquePaths(3, 7))  # Output: 28
print(solution.uniquePaths(3, 2))  # Output: 3  
print(solution.uniquePaths(1, 5))  # Output: 1

"""walkthrough
1. The function uniquePaths takes two integers m and n as input, representing the dimensions of the grid.
2. If either m or n is 1, it means there is only one path from the top-left corner to the bottom-right corner, so we return 1.
3. If m is less than n, we swap m and n to ensure that m is always greater than or equal to n. This is done to optimize the calculation of the number of unique paths.
4. We initialize two variables, res and j, to 1. res will store the result of the calculation, and j will be used to keep track of the denominator in the calculation.
5. We use a for loop to iterate from m to m + n - 1.    
6. In each iteration, we multiply res by i (the current value in the loop) and then divide res by j (the current value of j). This is equivalent to calculating the binomial coefficient C(m + n - 2, m - 1) or C(m + n - 2, n - 1), which gives us the number of unique paths from the top-left corner to the bottom-right corner.
7. After the loop, we return the value of res, which represents the number of unique paths from the top-left corner to the bottom-right corner.
8. The time complexity of this algorithm is O(m + n) due to the loop that iterates from m to m + n - 1, and the space complexity is O(1) since we are using only a constant amount of extra space for the variables res and j.
""" 