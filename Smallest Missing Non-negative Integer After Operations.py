"""You are given a 0-indexed integer array nums and an integer value.

In one operation, you can add or subtract value from any element of nums.

For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
Return the maximum MEX of nums after applying the mentioned operation any number of times.

 

Example 1:

Input: nums = [1,-10,7,13,6,8], value = 5
Output: 4
Explanation: One can achieve this result by applying the following operations:
- Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
- Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
- Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.
Example 2:

Input: nums = [1,-10,7,13,6,8], value = 7
Output: 2
Explanation: One can achieve this result by applying the following operation:
- subtract value from nums[2] once to make nums = [1,-10,0,13,6,8]
The MEX of nums is 2. It can be shown that 2 is the maximum MEX we can achieve."""

#answer

from collections import Counter
class Solution:
    def findSmallestInteger(self, nums, value):
        cnt = Counter(((x % value) + value) % value for x in nums) 
        m = 0
        while True:
            r = m % value
            if cnt[r] > 0:
                cnt[r] -= 1
                m += 1
            else:
                return m

#example
s = Solution()
print(s.findSmallestInteger([1,-10,7,13,6,8], 5)) # Output: 4
print(s.findSmallestInteger([1,-10,7,13,6,8], 7)) # Output: 2
"""walkthrough
1. The function findSmallestInteger is defined within the Solution class.
2. It takes two parameters: nums (a list of integers) and value (an integer).
3. The function uses a Counter to count the occurrences of each remainder when the elements of nums are taken modulo value.
4. It initializes a variable m to track the smallest missing non-negative integer.
5. It enters a while loop that continues indefinitely until it finds the smallest missing integer.
6. Inside the loop, it calculates the remainder r of m when divided by value.
7. If there are occurrences of r in the counter, it decrements the count and increments m.
8. If there are no occurrences of r, it returns m as the smallest missing non-negative integer.
"""