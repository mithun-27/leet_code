"""You are given a positive number n.

Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits

 

Example 1:

Input: n = 5

Output: 7

Explanation:

The binary representation of 7 is "111".

Example 2:

Input: n = 10

Output: 15

Explanation:

The binary representation of 15 is "1111".

Example 3:

Input: n = 3

Output: 3

Explanation:

The binary representation of 3 is "11".

 

Constraints:

1 <= n <= 1000"""


#answer
class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1
    
# Example usage:
sol = Solution()
print(sol.smallestNumber(5))  # Output: 7
print(sol.smallestNumber(10))  # Output: 15
print(sol.smallestNumber(3))   # Output: 3

"""walkthrough
You are given a positive number n.
Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits
The problem requires us to find the smallest number x that is greater than or equal to n, where x has all bits set in its binary representation.
To solve this problem, we can use the following approach:
1. Determine the number of bits required to represent n in binary. This can be done using the bit_length() method in Python, which returns the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros.
2. Calculate the smallest number with all bits set for the determined bit length. This can be
   achieved by left-shifting 1 by the bit length and then subtracting 1. The expression (1 << n.bit_length()) - 1 gives us a number with all bits set for the required length.
3. Return the calculated number.
class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1"""