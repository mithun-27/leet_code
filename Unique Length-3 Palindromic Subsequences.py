"""Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
 

Constraints:

3 <= s.length <= 105
s consists of only lowercase English letters."""

#answer

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for ch in map(chr, range(ord('a'), ord('z') + 1)):
            i = s.find(ch)
            j = s.rfind(ch)
            if i != -1 and j != -1 and i < j:
                mid_set = set(s[i+1:j])
                ans += len(mid_set)
        return ans

#sample test case
solution = Solution()
print(solution.countPalindromicSubsequence("aabca"))  # Output: 3
print(solution.countPalindromicSubsequence("adc"))    # Output: 0
print(solution.countPalindromicSubsequence("bbcbaba")) # Output: 4

"""walkthrough
1. Initialize a counter `ans` to zero to keep track of the number of unique palindromic subsequences.
2. Loop through each character `ch` from 'a' to 'z':
   a. Find the first occurrence index `i` and the last occurrence index `j` of `ch` in the string `s`.
   b. If both indices are valid and `i` is less than `j`, it means there are characters between these two occurrences.
   c. Create a set of characters found between indices `i` and `j` (exclusive) to ensure uniqueness.
   d. Add the size of this set to the counter `ans`.
3. Return the final count `ans` after checking all characters.
4. This approach efficiently counts unique palindromic subsequences of length 3 by leveraging the properties of palindromes and sets."""