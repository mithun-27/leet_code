"""Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res

#example usage
# Constructing the binary tree [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
solution = Solution()
print(solution.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]

"""walthrough
1. Initialize an empty list res to store the final level order traversal result.
2. Use a deque (double-ended queue) q to facilitate level order traversal. Start by appending the root node to q.
3. While q is not empty, do the following:
   a. Determine the number of nodes at the current level (qLen).
   b. Initialize an empty list level to store the values of nodes at the current level.
   c. For each node at the current level (from 0 to qLen-1):
      i. Pop the leftmost node from q.
      ii. If the node is not None, append its value to level and add its left and right children to q.
   d. If level is not empty, append it to res.
4. Return res as the final result."""