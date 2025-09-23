"""Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0"""

#answer:


class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]   
        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len


j = Solution()
print(j.longestValidParentheses("(()"))          # Output: 2
print(j.longestValidParentheses(")()())"))       # Output: 4
print(j.longestValidParentheses(""))              # Output: 0

"""walkthrough:
1. We define a class `Solution` with a method `longestValidParentheses` that takes a string `s` containing only '(' and ')'.
2. We initialize a stack with -1 to help calculate the lengths of valid parentheses substrings. The -1 serves as a base index for the first valid substring.
3. We also initialize `max_len` to keep track of the maximum length of valid parentheses found.
4. We iterate through each character in the string along with its index using `enumerate`.
5. If the character is '(', we push its index onto the stack.
6. If the character is ')', we pop the top index from the stack. If the stack becomes empty after popping, it means there is no matching '(', so we push the current index onto the stack as a new base. If the stack is not empty, we calculate the length of the current valid substring by subtracting the index at the new top of the stack from the current index and update `max_len` if this length is greater than the current `max_len`.
7. Finally, we return `max_len`, which contains the length of the longest valid parentheses substring found in the input string.
"""