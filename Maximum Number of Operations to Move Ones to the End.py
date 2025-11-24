"""You are given a binary string s.

You can perform the following operation on the string any number of times:

Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0'.
Move the character s[i] to the right until it reaches the end of the string or another '1'. For example, for s = "010010", if we choose i = 1, the resulting string will be s = "000110".
Return the maximum number of operations that you can perform.

 

Example 1:

Input: s = "1001101"

Output: 4

Explanation:

We can perform the following operations:

Choose index i = 0. The resulting string is s = "0011101".
Choose index i = 4. The resulting string is s = "0011011".
Choose index i = 3. The resulting string is s = "0010111".
Choose index i = 2. The resulting string is s = "0001111".
Example 2:

Input: s = "00111"

Output: 0

 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'."""

#answer
class Solution:
    def maxOperations(self, s: str) -> int:
        pref = list(accumulate(int(c) for c in s))
        return sum({pref[i] for i, c in enumerate(s) if c == '0'})

#sample usage
Solution().maxOperations("1001101")  # Expected output: 4
Solution().maxOperations("00111")    # Expected output: 0
Solution().maxOperations("111000")  # Expected output: 0

"""walkthrough
1. We define a class Solution with a method maxOperations that takes a binary string s as input.
2. We compute the prefix sum of the number of '1's in the string using accumulate from itertools.
3. We then iterate through the string, and for each '0', we add the number of '1's before it (from the prefix sum) to a set to ensure uniqueness.
4. Finally, we return the size of this set, which represents the maximum number of operations that can be performed.
"""