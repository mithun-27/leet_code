class Solution:
    def totalMoney(self, n: int) -> int:
        w, r = divmod(n, 7)
        full = 7 * w * (w - 1) // 2 + 28 * w
        rem  = r * w + r * (r + 1) // 2
        return full + rem
