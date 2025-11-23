from typing import List
import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones > 0:
            return n - ones

        
        INF = 10**9
        min_len_minus1 = INF  
        for i in range(n):
            g = nums[i]
            if g == 1:
                min_len_minus1 = 0
                break
            for j in range(i+1, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_len_minus1 = min(min_len_minus1, j - i)
                    break  

        if min_len_minus1 == INF:
            return -1

        
        return min_len_minus1 + (n - 1)
