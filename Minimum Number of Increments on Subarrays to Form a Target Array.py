"""You are given an integer array target. You have an integer array initial of the same size as target with all elements initially zeros.

In one operation you can choose any subarray from initial and increment each value by one.

Return the minimum number of operations to form a target array from initial.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: target = [1,2,3,2,1]
Output: 3
Explanation: We need at least 3 operations to form the target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.
Example 2:

Input: target = [3,1,1,2]
Output: 4
Explanation: [0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2]
Example 3:

Input: target = [3,1,5,4,2]
Output: 7
Explanation: [0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2].
 

Constraints:

1 <= target.length <= 105
1 <= target[i] <= 105
​​​​​​​The input is generated such that the answer fits inside a 32 bit integer."""

#answer

from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if not target:
            return 0
        ans = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i-1]:
                ans += target[i] - target[i-1]
        return ans

# Example usage:
sol = Solution()
print(sol.minNumberOperations([1,2,3,2,1]))  # Output: 3
print(sol.minNumberOperations([3,1,1,2]))     # Output: 4
print(sol.minNumberOperations([3,1,5,4,2]))   # Output: 7


"""walkthrough:
1. You are given an integer array target. You have an integer array initial of the same size as target with all elements initially zeros.
2. In one operation you can choose any subarray from initial and increment each value by one.
3. The goal is to determine the minimum number of operations required to transform initial into target.
4. To achieve this, we can use a greedy approach by focusing on the differences between consecutive elements in the target array.
5. We start by initializing the answer with the value of the first element in target, as we need at least that many operations to reach that value from zero.
6. We then iterate through the target array starting from the second element. For each element, if it is greater than the previous element, we add the difference to our answer. This is because we need to perform additional operations to reach this higher value.
7. Finally, we return the accumulated answer which represents the minimum number of operations needed to form the target array from the initial array.
Here is the implementation of the above logic in Python:from typing import List
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:    
        if not target:
            return 0
        ans = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i-1]:
                ans += target[i] - target[i-1]
        return ans
"""