"""Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
    
#example usage
sol = Solution()
# Example 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(sol.maxDepth(root1))  # Output: 3
# Example 2
root2 = TreeNode(1)
root2.right = TreeNode(2)
print(sol.maxDepth(root2))  # Output: 2

""""walkthrough
1. Initialize a queue to perform level-order traversal (BFS).
2. If the root is not None, add it to the queue.
3. Initialize a variable 'level' to keep track of the depth.
4. While the queue is not empty:
   a. For each node in the current level (determined by the current size of the queue):
      i. Dequeue a node.
      ii. If the node has a left child, enqueue it.
      iii. If the node has a right child, enqueue it.
   b. After processing all nodes at the current level, increment the 'level' counter.
5. Once the queue is empty, return the 'level' counter, which represents the maximum depth of the binary tree.
"""