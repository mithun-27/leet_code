"""You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length"""

#answer
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
    
#example usage
solution = Solution()
print(solution.characterReplacement("ABAB", 2))  # Output: 4
print(solution.characterReplacement("AABABBA", 1))  # Output: 4

"""walkthrough
1. Initialize a dictionary `count` to keep track of the frequency of each character in the current window.
2. Initialize variables `res` to store the length of the longest valid substring found, `l` (left pointer) to represent the start of the current window, and `maxf` to store the maximum frequency of any single character in the current window.
3. Loop through the string with the `r` pointer (right pointer):
    - Update the frequency count of the character at index `r` in the `count` dictionary.
    - Update `maxf` to be the maximum frequency of any character in the current window.
    - Check if the number of characters that need to be replaced to make all characters in the window the same (i.e., `(r - l + 1) - maxf`) exceeds `k`. If it does, it means we need to shrink the window from the left:
        - Decrease the frequency count of the character at index `l` in the `count` dictionary.
        - Increment `l` to shrink the window.
    - Update `res` with the maximum value between the current `res` and the length of the current valid window (`r - l + 1`).
4. After the loop, return `res`, which contains the length of the longest substring that can be formed with at most `k` replacements.
5. This approach ensures that each character is processed at most twice (once added and once removed), resulting in an O(n) time complexity.
"""