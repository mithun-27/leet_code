"""You are given an array nums of size n, consisting of non-negative integers. Your task is to apply some (possibly zero) operations on the array so that all elements become 0.

In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n) and set all occurrences of the minimum non-negative integer in that subarray to 0.

Return the minimum number of operations required to make all elements in the array 0.

 

Example 1:

Input: nums = [0,2]

Output: 1

Explanation:

Select the subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0].
Thus, the minimum number of operations required is 1.
Example 2:

Input: nums = [3,1,2,1]

Output: 3

Explanation:

Select subarray [1,3] (which is [1,2,1]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [3,0,2,0].
Select subarray [2,2] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [3,0,0,0].
Select subarray [0,0] (which is [3]), where the minimum non-negative integer is 3. Setting all occurrences of 3 to 0 results in [0,0,0,0].
Thus, the minimum number of operations required is 3.
Example 3:

Input: nums = [1,2,1,2,1,2]

Output: 4

Explanation:

Select subarray [0,5] (which is [1,2,1,2,1,2]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [0,2,0,2,0,2].
Select subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,2,0,2].
Select subarray [3,3] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,0,0,2].
Select subarray [5,5] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,0,0,0].
Thus, the minimum number of operations required is 4.
 

Constraints:

1 <= n == nums.length <= 105
0 <= nums[i] <= 105"""

#answer
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        st = [0]  

        for x in nums:
            while st and st[-1] > x:
                st.pop()
            if not st or st[-1] < x:
                ans += 1
                st.append(x)

        return ans

#example usage
s = Solution()
print(s.minOperations([0, 2]))  # Output: 1
print(s.minOperations([3, 1, 2, 1]))  # Output: 3
print(s.minOperations([1, 2, 1, 2, 1, 2]))  # Output: 4

"""walthrough of the code 
1. The `Solution` class is defined with a method `minOperations` that takes a list of integers `nums`.
2. The variable `ans` is initialized to 0, which will count the number of operations needed.
3. A stack `st` is initialized with a single element 0, which will be used to keep track of the minimum elements encountered.
4. The method iterates through each element `x` in `nums`.
5. Inside the loop, a while loop checks if the top of the stack `st` is greater than `x`. If it is, the top element is popped from the stack.
6. If the stack is empty or the top element of the stack is less than `x`, it means `x` is a new minimum that needs to be counted. The operation count `ans` is incremented by 1, and `x` is pushed onto the stack.
7. After processing all elements in `nums`, the method returns the total count of operations stored in `ans`.
This approach ensures that we only count unique minimums in the sequence, leading to the minimum number of operations required to convert all elements to zero.
"""