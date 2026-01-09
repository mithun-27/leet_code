"""Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 10"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
    
#example usage
sol = Solution()
# Example 1
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(7)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(9)
inverted1 = sol.invertTree(root1)
# Example 2
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
inverted2 = sol.invertTree(root2)
# Example 3
root3 = None
inverted3 = sol.invertTree(root3)



""""walkthrough
1. Check if the root is None. If it is, return None.
2. Initialize a stack with the root node.       
3. While the stack is not empty:
   a. Pop a node from the stack.
   b. Swap its left and right children.
   c. If the left child exists, push it onto the stack.
   d. If the right child exists, push it onto the stack.
4. Return the root of the inverted tree.
5. This approach uses an iterative method with a stack to traverse the tree and swap the children of each node, effectively inverting the binary tree.
"""
