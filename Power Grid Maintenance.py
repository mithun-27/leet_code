"""You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).

These stations are interconnected via n bidirectional cables, represented by a 2D array connections, where each element connections[i] = [ui, vi] indicates a connection between station ui and station vi. Stations that are directly or indirectly connected form a power grid.

Initially, all stations are online (operational).

You are also given a 2D array queries, where each query is one of the following two types:

[1, x]: A maintenance check is requested for station x. If station x is online, it resolves the check by itself. If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x. If no operational station exists in that grid, return -1.

[2, x]: Station x goes offline (i.e., it becomes non-operational).

Return an array of integers representing the results of each query of type [1, x] in the order they appear.

Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.

 

Example 1:

Input: c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

Output: [3,2,3]

Explanation:



Initially, all stations {1, 2, 3, 4, 5} are online and form a single power grid.
Query [1,3]: Station 3 is online, so the maintenance check is resolved by station 3.
Query [2,1]: Station 1 goes offline. The remaining online stations are {2, 3, 4, 5}.
Query [1,1]: Station 1 is offline, so the check is resolved by the operational station with the smallest id among {2, 3, 4, 5}, which is station 2.
Query [2,2]: Station 2 goes offline. The remaining online stations are {3, 4, 5}.
Query [1,2]: Station 2 is offline, so the check is resolved by the operational station with the smallest id among {3, 4, 5}, which is station 3.
Example 2:

Input: c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]

Output: [1,-1]

Explanation:

There are no connections, so each station is its own isolated grid.
Query [1,1]: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1.
Query [2,1]: Station 1 goes offline.
Query [1,1]: Station 1 is offline and there are no other stations in its grid, so the result is -1."""

#answer

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

#example usage
solution = Solution()
print(solution.processQueries(5, [[1,2],[2,3],[3,4],[4,5]], [[1,3],[2,1],[1,1],[2,2],[1,2]]))  # Output: [3,2,3]
print(solution.processQueries(3, [], [[1,1],[2,1],[1,1]]))  # Output: [1,-1]
print(solution.processQueries(4, [[1,2],[2,3]], [[1,4],[2,2],[1,2],[1,3]]))  # Output: [4,3,3]


