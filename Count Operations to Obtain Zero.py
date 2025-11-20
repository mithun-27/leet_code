"""You are given two non-negative integers num1 and num2.

In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.

For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.
Return the number of operations required to make either num1 = 0 or num2 = 0.

 

Example 1:

Input: num1 = 2, num2 = 3
Output: 3
Explanation: 
- Operation 1: num1 = 2, num2 = 3. Since num1 < num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
- Operation 2: num1 = 2, num2 = 1. Since num1 > num2, we subtract num2 from num1.
- Operation 3: num1 = 1, num2 = 1. Since num1 == num2, we subtract num2 from num1.
Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need to perform any further operations.
So the total number of operations required is 3.
Example 2:

Input: num1 = 10, num2 = 10
Output: 1
Explanation: 
- Operation 1: num1 = 10, num2 = 10. Since num1 == num2, we subtract num2 from num1 and get num1 = 10 - 10 = 0.
Now num1 = 0 and num2 = 10. Since num1 == 0, we are done.
So the total number of operations required is 1.
 

Constraints:

0 <= num1, num2 <= 105"""

#answer
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        a, b = num1, num2
        ops = 0
        while a and b:
            if a < b:
                a, b = b, a
            ops += a // b
            a %= b
        return ops

#example usage
s = Solution()
print(s.countOperations(2, 3))  # Output: 3
print(s.countOperations(10, 10))  # Output: 1


"""walkthrough of the code:
1. Initialize a and b with num1 and num2 respectively, and ops to 0 to count the operations.
2. While both a and b are non-zero, do the following:
   a. If a is less than b, swap their values.
   b. Increment ops by the integer division of a by b (this counts how many times we can subtract b from a).
   c. Update a to be the remainder of a divided by b (this simulates the subtraction).
3. Return ops as the total number of operations performed.
"""