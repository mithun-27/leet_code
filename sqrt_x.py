"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned."""

#answer:

class Solution:
    def mySqrt(self, x):
        if x < 2:  
            return x

        left, right = 1, x // 2  

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right 

j = Solution()
print(j.mySqrt(4))
print(j.mySqrt(8))
print(j.mySqrt(0))
print(j.mySqrt(1))


"""walkthrough:
1. We define a class `Solution` with a method `mySqrt` that takes a non-negative integer `x`.
2. We handle the base cases where `x` is less than 2, returning `x` directly since the square root of 0 is 0 and the square root of 1 is 1.
3. We initialize two pointers, `left` and `right`. `left` starts at 1 and `right` starts at `x // 2` because the square root of `x` cannot be more than `x / 2` for `x >= 2`.
4. We use a while loop to perform binary search until `left` exceeds `right`.   
5. In each iteration, we calculate the midpoint `mid` and check if `mid * mid` equals `x`. If it does, we return `mid` as the square root.
6. If `mid * mid` is less than `x`, we move the `left` pointer to `mid + 1` to search in the higher half. If `mid * mid` is greater than `x`, we move the `right` pointer to `mid - 1` to search in the lower half.
7. If we exit the loop, `right` will be the largest integer whose square is less than or equal to `x`, so we return `right`.
"""