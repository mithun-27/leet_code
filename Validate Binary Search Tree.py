"""Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True

#example usage
# Constructing the binary tree [2,1,3]  
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
solution = Solution()
print(solution.isValidBST(root))  # Output: True

"""walkthrough
1. We define a class Solution with a method isValidBST that takes the root of a binary tree as input.
2. We check if the root is None; if it is, we return True since an empty tree is a valid BST.
3. We initialize a deque (double-ended queue) to perform a breadth-first traversal of the tree. Each element in the queue is a tuple containing a node and its valid value range (left, right).
4. We enter a while loop that continues until the queue is empty. In each iteration, we pop the leftmost element from the queue.
5. We check if the current node's value is within the valid range (left < node.val < right). If it is not, we return False.
6. If the current node has a left child, we append it to the queue with an updated valid range (left, node.val). Similarly, if it has a right child, we append it with the range (node.val, right).
7. If we finish processing all nodes without finding any violations of the BST properties, we return True.
8. The example usage constructs a simple binary tree and checks if it is a valid BST, printing the result.
"""