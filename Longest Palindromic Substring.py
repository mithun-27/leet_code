"""Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters."""

#answer
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s):
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            p = [0] * n
            l, r = 0, 0
            for i in range(n):
                p[i] = min(r - i, p[l + (r - i)]) if i < r else 0
                while (i + p[i] + 1 < n and i - p[i] - 1 >= 0
                       and t[i + p[i] + 1] == t[i - p[i] - 1]):
                    p[i] += 1
                if i + p[i] > r:
                    l, r = i - p[i], i + p[i]
            return p

        p = manacher(s)
        resLen, center_idx = max((v, i) for i, v in enumerate(p))
        resIdx = (center_idx - resLen) // 2
        return s[resIdx : resIdx + resLen]
    
#example usage
print(Solution().longestPalindrome("babad"))  # Example call to the function
print(Solution().longestPalindrome("cbbd"))  # Example call to the function
# Output: "bab" or "aba"

"""walkthrough
1. We define a class Solution with a method longestPalindrome that takes a string s as input.
2. Inside the method, we define a helper function manacher that implements Manacher's algorithm to find the lengths of palindromic substrings centered at each character in a transformed string.   
3. The transformed string t is created by inserting '#' characters between each character of s and at the beginning and end. This helps to handle even-length palindromes uniformly.    
4. We initialize an array p to store the lengths of palindromic substrings and two pointers l and r to keep track of the rightmost palindrome found so far. 
5. We iterate through each character in the transformed string t, updating the lengths of palindromic substrings in p using previously computed values and expanding around the center as needed.   
6. After computing the array p, we find the maximum length of the palindrome and its center index.  
7. We calculate the starting index of the longest palindromic substring in the original string s and return the substring.
"""