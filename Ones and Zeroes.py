"""You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100"""

#answer
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]

        for s in strs:
            z = s.count('0')
            o = len(s) - z
            for i in range(m, z-1, -1):
                for j in range(n, o-1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - z][j - o])

        return dp[m][n]

# Example usage:
solution = Solution()
print(solution.findMaxForm(["10","0001","111001","1","0"], 5, 3))  # Output: 4
print(solution.findMaxForm(["10","0","1"], 1, 1))  # Output: 2
print(solution.findMaxForm(["10","0001","111001","1","0"], 3, 3))  # output: 3

"""walkthrough
1. We define a class Solution with a method findMaxForm that takes a list of binary strings strs and two integers m and n.
2. We initialize a 2D list dp with dimensions (m+1) x (n+1) filled with zeros. This will be used for dynamic programming to store the maximum subset sizes.
3. We iterate through each string s in strs.
4. For each string, we count the number of '0's (z) and '1's (o).
5. We then update the dp table in reverse order to avoid overwriting values that we still need to use.
6. Finally, we return the value at dp[m][n], which contains the size of the largest subset that can be formed with at most m '0's and n '1's.
"""