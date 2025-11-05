"""Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

 

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96."""


#answer
class Solution:
    def totalMoney(self, n: int) -> int:
        w, r = divmod(n, 7)
        full = 7 * w * (w - 1) // 2 + 28 * w
        rem  = r * w + r * (r + 1) // 2
        return full + rem

#example usage
solution = Solution()
print(solution.totalMoney(4))  # Output: 10
print(solution.totalMoney(10))  # Output: 37
print(solution.totalMoney(20))  # Output: 96

"""walkthrough of the code:
1. The function totalMoney takes an integer n as input, representing the number of days Hercy saves money.
2. It calculates the number of complete weeks (w) and the remaining days (r) using divmod.
3. The variable full calculates the total amount saved during the complete weeks using the formula for the sum of an arithmetic series.
4. The variable rem calculates the total amount saved during the remaining days after the complete weeks.
5. Finally, the function returns the sum of full and rem, which is the total amount saved after n days.
"""