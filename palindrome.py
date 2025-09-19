"""Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome."""

#answer:

class Solution(object):
    def isPalindrome(self, x):
       y=str(x)
       return y == y[::-1]
j = Solution()
print(j.isPalindrome(121))

#or

def is_palindrome_number(n):
    original = n
    reversed_num = 0

    while n > 0:
        digit = n % 10                 # get last digit
        reversed_num = reversed_num * 10 + digit
        n = n // 10                    # remove last digit

    return original == reversed_num

print(is_palindrome_number(121))   
print(is_palindrome_number(1331))  
print(is_palindrome_number(123))   
print(is_palindrome_number(10))    