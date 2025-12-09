"""There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

You are also given a 0-indexed integer array values of length n, where values[i] is the value associated with the ith node, and an integer k.

A valid split of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by k, where the value of a connected component is the sum of the values of its nodes.

Return the maximum number of components in any valid split.

 

Example 1:


Input: n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6
Output: 2
Explanation: We remove the edge connecting node 1 with 2. The resulting split is valid because:
- The value of the component containing nodes 1 and 3 is values[1] + values[3] = 12.
- The value of the component containing nodes 0, 2, and 4 is values[0] + values[2] + values[4] = 6.
It can be shown that no other valid split has more than 2 connected components.
Example 2:


Input: n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3
Output: 3
Explanation: We remove the edge connecting node 0 with 2, and the edge connecting node 0 with 1. The resulting split is valid because:
- The value of the component containing node 0 is values[0] = 3.
- The value of the component containing nodes 2, 5, and 6 is values[2] + values[5] + values[6] = 9.
- The value of the component containing nodes 1, 3, and 4 is values[1] + values[3] + values[4] = 6.
It can be shown that no other valid split has more than 3 connected components.
 

Constraints:

1 <= n <= 3 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
values.length == n
0 <= values[i] <= 109
1 <= k <= 109
Sum of values is divisible by k.
The input is generated such that edges represents a valid tree."""


#answer

from typing import List
import sys
sys.setrecursionlimit(10**7)

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        self.ans = 0

        def dfs(u: int, parent: int) -> int:
         
            total = values[u] % k
            for v in g[u]:
                if v == parent:
                    continue
                child_sum = dfs(v, u)
                total = (total + child_sum) % k

            if total % k == 0:
               
                self.ans += 1
                return 0  
            return total

        dfs(0, -1)
        return self.ans

#sample test case
solution = Solution()
print(solution.maxKDivisibleComponents(5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6))  # Output: 2
print(solution.maxKDivisibleComponents(7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [3,0,6,1,5,2,1], 3))  # Output: 3


"""walkthrough
1. Construct an adjacency list `g` to represent the tree from the given edges.
2. Initialize a variable `self.ans` to keep track of the number of valid components.
3. Define a recursive DFS function that takes the current node `u` and its parent node `parent` as arguments.
   a. Initialize `total` to the value of the current node modulo `k`.
    b. Iterate through the neighbors `v` of node `u`. If `v` is the parent, skip it.
        i. Recursively call DFS on child node `v` and add the returned value to `total`, taking modulo `k`.
    c. After processing all children, check if `total` modulo `k` is 0:
        i. If it is, increment `self.ans` by 1 and return 0 to indicate that this subtree can be considered a separate component.
        ii. If not, return `total` to propagate the sum up the tree.
4. Start the DFS from the root node (0) with a parent of -1.
5. Finally, return `self.ans`, which contains the maximum number of k-divisible components.
""""