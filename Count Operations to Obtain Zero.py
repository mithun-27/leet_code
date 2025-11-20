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
