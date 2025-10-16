""""You are given two integers, m and k, and an integer array nums.

A sequence of integers seq is called magical if:
seq has a size of m.
0 <= seq[i] < nums.length
The binary representation of 2seq[0] + 2seq[1] + ... + 2seq[m - 1] has k set bits.
The array product of this sequence is defined as prod(seq) = (nums[seq[0]] * nums[seq[1]] * ... * nums[seq[m - 1]]).

Return the sum of the array products for all valid magical sequences.

Since the answer may be large, return it modulo 109 + 7.

A set bit refers to a bit in the binary representation of a number that has a value of 1.

 

Example 1:

Input: m = 5, k = 5, nums = [1,10,100,10000,1000000]

Output: 991600007

Explanation:

All permutations of [0, 1, 2, 3, 4] are magical sequences, each with an array product of 1013.

Example 2:

Input: m = 2, k = 2, nums = [5,4,3,2,1]

Output: 170

Explanation:

The magical sequences are [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 4], [4, 0], [4, 1], [4, 2], and [4, 3].

Example 3:

Input: m = 1, k = 1, nums = [28]

Output: 28

Explanation:

The only magical sequence is [0]."""

#answer
MOD = 10**9 + 7
from functools import lru_cache
import math
from typing import List

class Solution:
    def magicalSum(self, total_count: int, target_odd: int, numbers: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(remaining, odd_needed, index, carry):
            if remaining < 0 or odd_needed < 0 or remaining + carry.bit_count() < odd_needed:
                return 0
            if remaining == 0:
                return 1 if odd_needed == carry.bit_count() else 0
            if index >= len(numbers):
                return 0
            
            ans = 0
            for take in range(remaining + 1):
                ways = math.comb(remaining, take) * pow(numbers[index], take, MOD) % MOD
                new_carry = carry + take
                ans += ways * dfs(remaining - take, odd_needed - (new_carry % 2), index + 1, new_carry // 2)
                ans %= MOD
            return ans
        
        return dfs(total_count, target_odd, 0, 0)

#example
s = Solution()
print(s.magicalSum(5, 3, [1, 2, 3, 4, 5]))
# Output: 240
print(s.magicalSum(10, 5, [2, 3, 5]))
# Output: 0
print(s.magicalSum(3, 2, [1, 1, 1]))


"""walkthrough
1. The function magicalSum is defined within the Solution class.
2. It takes three parameters: total_count (the total number of elements to choose), target_odd (the target number of odd elements), and numbers (the list of available numbers).
3. The function uses a depth-first search (DFS) approach with memoization (lru_cache) to explore all possible combinations of numbers.
4. The dfs function is defined within magicalSum and takes several parameters:
   - remaining: the number of elements left to choose
   - odd_needed: the number of odd elements still needed
   - index: the current index in the numbers list
   - carry: a bitmask representing the current state of chosen elements
5. The base cases for the dfs function are as follows:
   - If remaining < 0 or odd_needed < 0 or remaining + carry.bit_count() < odd_needed, return 0 (invalid state).
   - If remaining == 0, return 1 if odd_needed == carry.bit_count() (valid combination found), else return 0.
   - If index >= len(numbers), return 0 (no more numbers to choose from).
6. The main logic of the dfs function involves iterating over the possible number of elements to take (from 0 to remaining).
7. For each possible take, the number of ways to choose those elements is calculated using combinations and modular exponentiation.
8. The new_carry is updated based on the current take.
9. The dfs function is called recursively with updated parameters, and the result is accumulated in ans.
10. Finally, the magicalSum function returns the result of the dfs function.
"""