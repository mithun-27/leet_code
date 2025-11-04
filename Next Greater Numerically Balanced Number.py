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
