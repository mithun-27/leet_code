"""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6."""

#answer:

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if not words:
            return 0
        return len(words[-1])
    
j = Solution()
print(j.lengthOfLastWord("Hello World"))  # Output: 5
print(j.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(j.lengthOfLastWord("luffy is still joyboy"))  # Output: 6


"""walkthrough:
1. We start by splitting the input string `s` into a list of words using the `split()` method, which automatically handles multiple spaces and trims leading/trailing spaces.
2. We check if the list of words is empty. If it is, we return
0, as there are no words in the string.
3. If the list is not empty, we access the last word using `words[-1]` and return its length using the `len()` function.
"""