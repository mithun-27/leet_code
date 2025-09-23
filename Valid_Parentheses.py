"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false"""


#answer:

class Solution:
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:                     
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:    
                    return False
            else:                               
                stack.append(char)
        return not stack


j = Solution()
print(j.isValid("()"))          # Output: True
print(j.isValid("()[]{}"))      # Output: True
print(j.isValid("(]"))          # Output: False
print(j.isValid("([])"))        # Output: True


"""walkthrough:
1. We define a class `Solution` with a method `isValid` that takes a
   string `s` containing only the characters '(', ')', '{', '}', '[' and ']'.
2. We initialize an empty list `stack` to use as a stack for tracking opening brackets
   and a dictionary `mapping` to map each closing bracket to its corresponding opening bracket.
3. We iterate through each character in the string `s`.
4. If the character is a closing bracket (i.e., it exists in the `mapping` dictionary), we check if the stack is not empty and pop the top element from the stack. If the stack is empty, we assign a dummy value '#' to `top_element`.
5. We then compare the popped element (or dummy value) with the corresponding opening bracket from the `mapping` dictionary. If they do not match, we return `False`, indicating that the string is not valid.
6. If the character is an opening bracket, we push it onto the stack.
7. After processing all characters, we check if the stack is empty. If it is empty, it means all opening brackets had matching closing brackets in the correct order, so we return `True`. If the stack is not empty, we return `False`, indicating that there are unmatched opening brackets.
"""