"""Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters."""

#answer
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

#example usage
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(solution.minWindow("a", "a"))  # Output: "a"
print(solution.minWindow("a", "aa"))  # Output: ""

"""walkthrough
1. Check if the target string `t` is empty. If it is, return an empty string.
2. Create two dictionaries: `countT` to store the frequency of each character in `t`, and `window` to store the frequency of characters in the current window of `s`.
3. Initialize variables `have` and `need` to keep track of how many unique characters from `t` are currently satisfied in the window and how many unique characters are needed, respectively.
4. Initialize `res` to store the start and end indices of the minimum window found, and `resLen` to store the length of that window (initialized to infinity).
5. Use a sliding window approach with two pointers, `l` (left) and `r` (right):
    - Expand the window by moving the `r` pointer and updating the frequency of the character at `s[r]` in the `window` dictionary.
    - If the character at `s[r]` is in `countT` and its frequency in `window` matches that in `countT`, increment `have`.
    - While `have` equals `need`, it means the current window contains all characters from `t`:
        - Check if the current window size is smaller than `resLen`. If it is, update `res` and `resLen`.
        - Shrink the window from the left by decrementing the frequency of the character at `s[l]` in `window`. If this character is in `countT` and its frequency in `window` drops below that in `countT`, decrement `have`.
        - Move the left pointer `l` to the right.
6. After processing the entire string `s`, extract the substring using the indices stored in `res`. If no valid window was found, return an empty string.
"""