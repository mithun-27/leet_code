"""An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

Given an integer n, return the smallest numerically balanced number strictly greater than n.

 

Example 1:

Input: n = 1
Output: 22
Explanation: 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
Example 2:

Input: n = 1000
Output: 1333
Explanation: 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
Example 3:

Input: n = 3000
Output: 3133
Explanation: 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000."""

#answer
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(x: int) -> bool:
            cnt = [0]*10
            while x:
                d = x % 10
                if d == 0:  
                    return False
                cnt[d] += 1
                x //= 10
            for d in range(1, 10):
                if cnt[d] not in (0, d):
                    return False
            return True

        x = n + 1
        while True:
            if is_balanced(x):
                return x
            x += 1


#example usage
solution = Solution()
print(solution.nextBeautifulNumber(1))     # Output: 22
print(solution.nextBeautifulNumber(1000))  # Output: 1333
print(solution.nextBeautifulNumber(3000))  # Output: 3133


"""walkthrough
1. Define a helper function is_balanced(x) that checks if a number x is numerically balanced.
2. In is_balanced, count the occurrences of each digit in x using an array cnt.
3. Check if the count of each digit matches its value (e.g., digit 2 appears 2 times).
4. In the main function, incrementally search for the next beautiful number by checking each subsequent integer.
"""