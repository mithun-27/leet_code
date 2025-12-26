"""Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces."""


#answer
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


#example usage
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3

"""walkthrough
1. Initialize an empty set `charSet` to keep track of unique characters in the current substring.
2. Initialize two pointers, `l` (left) and `r` (right), to represent the current substring's boundaries. Start with `l` at index 0.
3. Initialize a variable `res` to keep track of the length of the longest substring found so far, starting at 0.
4. Loop through the string with the `r` pointer:
    - While the character at index `r` is already in `charSet`, it means we have a duplicate. Remove the character at index `l` from `charSet` and increment `l` to shrink the window from the left until the duplicate is removed.
    - Add the character at index `r` to `charSet`.
    - Update `res` with the maximum value between the current `res` and the length of the current substring (`r - l + 1`).
5. After the loop, return `res`, which contains the length of the longest substring without repeating characters.
6. This approach ensures that each character is processed at most twice (once added and once removed), resulting in an O(n) time complexity.from typing import List
"""