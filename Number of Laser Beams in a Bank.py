"""Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:

The two devices are located on two different rows: r1 and r2, where r1 < r2.
For each row i where r1 < i < r2, there are no security devices in the ith row.
Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.

 

Example 1:


Input: bank = ["011001","000000","010100","001000"]
Output: 8
Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0th row with any on the 3rd row.
This is because the 2nd row contains security devices, which breaks the second condition.
Example 2:


Input: bank = ["000","111","000"]
Output: 0
Explanation: There does not exist two devices located on two different rows."""

#answer
class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        prev = 0
        ans = 0
        for row in bank:
            curr = row.count('1')
            if curr:
                ans += prev * curr
                prev = curr
        return ans

#example usage
sol = Solution()
print(sol.numberOfBeams(["011001","000000","010100","001000"])) #8
print(sol.numberOfBeams(["000","111","000"])) #0 


"""Explanation of the code:
1. We initialize two variables: prev to keep track of the number of security devices in the previous non-empty row, and ans to accumulate the total number of laser beams.
2. We iterate through each row in the bank. For each row, we count the number of '1's (security devices) and store it in curr.
3. If curr is greater than 0 (meaning the current row has security devices), we calculate the number of laser beams formed between the current row and the previous non-empty row by multiplying prev and curr, and add this to ans.
4. We then update prev to be curr for the next iteration.
5. Finally, we return ans, which contains the total number of laser beams in the bank.
"""