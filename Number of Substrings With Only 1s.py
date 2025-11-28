"""Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
"""

#answer
class Solution:
    def numSub(self, s: str) -> int:
        mod=10**9+7
        count=0
        ans=0
        for c in s:
            is0=c=='0'
            ans+=(-is0 & count*(count+1)//2)
            ans%=mod
            count=(-(not is0) & count+1)
        ans=ans+count*(count+1)//2%mod
        return ans

        