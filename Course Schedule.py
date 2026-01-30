"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique."""

#answer
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finish == numCourses

#example usage
Solution().canFinish(2, [[1,0]])  # Example call to the function      
Solution().canFinish(2, [[1,0],[0,1]])  # Example call to the function
"""Example 1:
Input: adjList = [[2,4],[1,3],[2],[4],[]]
Output: [[2,4],[1,3],[2],[4],[]]
Explanation: There are 5 nodes in the graph. The node with val = 1 has two neighbors: 2 and 4. The node with val = 2 has one neighbor: 3. The node with val = 3 has one neighbor: 4. The node with val = 4 has no neighbors. The node with val = 5 has no neighbors. 
The graph looks like this: 1 -- 2
|     |         3       4                                                           
|     |         |       |
5 ----         4       5
Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors."""

"""walkthrough
1. Check for an empty input graph. If the input node is None, return None.
2. Create a mapping (dictionary) to keep track of the original nodes and their corresponding cloned nodes.
3. Initialize a queue for BFS traversal and add the starting node to it.
4. While the queue is not empty, do the following:
   a. Dequeue a node from the front of the queue.
   b. For each neighbor of the current node:
      i. If the neighbor has not been cloned yet (not in the mapping), create a clone and add it to the mapping and the queue.
      ii. Add the cloned neighbor to the neighbors list of the cloned current node.
      iii. Continue this process until all nodes have been cloned.
5. Finally, return the cloned node corresponding to the input node from the mapping.
   d. Append the cloned neighbor to the neighbors list of the cloned current node.
6. Finally, return the cloned node corresponding to the input node from the mapping.
7. The BFS ensures that all nodes are visited and cloned, maintaining the original graph structure in the cloned graph.
"""