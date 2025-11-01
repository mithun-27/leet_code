class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        from math import comb
        
        row_len = n - 2
        
        coeff = [comb(row_len, i) % 10 for i in range(row_len + 1)]
        
        num1 = 0
        for i in range(0, n-1):
            num1 = (num1 + coeff[i] * (ord(s[i]) - ord('0'))) % 10
        
        
        num2 = 0
        for i in range(1, n):
            num2 = (num2 + coeff[i-1] * (ord(s[i]) - ord('0'))) % 10
        
        return num1 == num2
