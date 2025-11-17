from typing import List
import heapq

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1


class Solution:
    def processQueries(self, n: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(n)

        # Build components
        for u, v in connections:
            dsu.union(u, v)

        # Min-heap per component
        comp = {}
        for node in range(1, n + 1):
            root = dsu.find(node)
            if root not in comp:
                comp[root] = []
            comp[root].append(node)

        for root in comp:
            heapq.heapify(comp[root])

        # Initially all stations online
        online = [True] * (n + 1)

        def get_min_online(x):
            root = dsu.find(x)
            h = comp[root]
            while h and not online[h[0]]:
                heapq.heappop(h)
            return h[0] if h else -1

        ans = []
        for t, x in queries:
            if t == 1:  # query smallest online in component
                if online[x]:
                    ans.append(x)
                else:
                    ans.append(get_min_online(x))
            else:  # t == 2 -> turn station offline
                online[x] = False

        return ans
