"""Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

 

Example 1:

Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.
Example 2:

Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.
Example 3:

Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.
 

Constraints:

1 <= k <= 105"""


#answer

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # If k has factor 2 or 5, impossible
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        rem = 0
        seen = set()

        for length in range(1, k + 1):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return length
            if rem in seen:
                return -1
            seen.add(rem)

        return -1

#sample test case
solution = Solution()
print(solution.smallestRepunitDivByK(1))  # Output: 1
print(solution.smallestRepunitDivByK(2))  # Output: -1
print(solution.smallestRepunitDivByK(3))  # Output: 3

"""walkthrough
1. Check if k is divisible by 2 or 5. If it is, return -1 since no such number can exist.
2. Initialize a variable `rem` to keep track of the current remainder when forming numbers made of 1's.
3. Initialize a set `seen` to keep track of remainders we have encountered to detect cycles.
4. Loop through lengths from 1 to k:
    a. Update `rem` to be the remainder of the number formed by appending a 1 (i.e., `rem = (rem * 10 + 1) % k`).
    b. If `rem` is 0, return the current length since we found a number divisible by k.
    c. If `rem` has been seen before, return -1 since we are in a cycle and won't find a solution.
    d. Add `rem` to the `seen` set.
5. If the loop completes without finding a solution, return -1.
"""