from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)

        def add_op(t: str) -> str:
            arr = list(t)
            for i in range(1, n, 2):  
                arr[i] = str((int(arr[i]) + a) % 10)
            return "".join(arr)

        def rotate_right(t: str) -> str:
            k = b % n
            if k == 0:
                return t
            return t[-k:] + t[:-k]

        best = s
        q = deque([s])
        seen = {s}

        while q:
            cur = q.popleft()
            if cur < best:
                best = cur

            t1 = add_op(cur)
            if t1 not in seen:
                seen.add(t1)
                q.append(t1)

            t2 = rotate_right(cur)
            if t2 not in seen:
                seen.add(t2)
                q.append(t2)

        return best