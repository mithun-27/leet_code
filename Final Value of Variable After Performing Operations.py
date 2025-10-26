"""There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

 

Example 1:

Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
Example 2:

Input: operations = ["++X","++X","X++"]
Output: 3
Explanation: The operations are performed as follows:
Initially, X = 0.
++X: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
X++: X is incremented by 1, X = 2 + 1 = 3.
Example 3:

Input: operations = ["X++","++X","--X","X--"]
Output: 0
Explanation: The operations are performed as follows:
Initially, X = 0.
X++: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
--X: X is decremented by 1, X = 2 - 1 = 1.
X--: X is decremented by 1, X = 1 - 1 = 0."""

#answer

class Solution:
    def finalValueAfterOperations(self, operations):
        x = 0
        for op in operations:
            if "++" in op:
                x += 1
            else:
                x -= 1
        return x
    
#answer
s=solution = Solution()
print(s.finalValueAfterOperations(["--X","X++","X++"]))  # Output: 1 
print(s.finalValueAfterOperations(["++X","++X","X++"]))  # Output: 3
print(s.finalValueAfterOperations(["X++","++X","--X","X--"]))  # Output: 0  

"""walkthrough
1. We define a class Solution with a method finalValueAfterOperations that takes a list of operations as input.
2. We initialize a variable x to 0, which will hold the final value of the variable X.
3. We iterate through each operation in the operations list.
4. For each operation, we check if it contains "++". If it does, we increment x by 1. Otherwise, we decrement x by 1.
5. Finally, we return the value of x after processing all operations.
"""