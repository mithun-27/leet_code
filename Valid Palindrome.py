"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters."""

#answer

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    
# Example usage:
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(solution.isPalindrome("race a car"))  # Output: False
print(solution.isPalindrome(" "))  # Output: True

"""walkthrough
1. We define a class Solution with a method isPalindrome that takes a string s as input.
2. We initialize two pointers, l and r, to the start and end of the string, respectively.
3. We enter a while loop that continues as long as l is less than r.
4. Inside the loop, we use two nested while loops to move the l pointer forward and the r pointer backward until they point to alphanumeric characters. This is done using the helper method alphaNum, which checks if a character is alphanumeric. 
5. After finding valid alphanumeric characters at both pointers, we compare them in a case-insensitive manner using the lower() method. If they do not match, we return False, indicating that the string is not a palindrome.  
6. If the characters match, we move both pointers closer to the center of the string (l is incremented and r is decremented) and continue the process.  
7. If the loop completes without finding any mismatches, we return True, indicating that the string is a palindrome.
"""