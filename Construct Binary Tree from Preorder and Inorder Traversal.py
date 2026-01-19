"""Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree."""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from logging import root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head
        i, j, n = 0, 0, len(preorder)
        while i < n and j < n:
            # Go right and then as far left as possible
            curr.right = TreeNode(preorder[i], right = curr.right)
            curr = curr.right
            i += 1
            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i += 1
            j += 1
            while curr.right and j < n and curr.right.val == inorder[j]:
                prev = curr.right
                curr.right = None
                curr = prev
                j += 1
        
        return head.right

#example usage
solution = Solution()   
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
tree = solution.buildTree(preorder, inorder)
root.right = TreeNode(4)
k = 1
solution = Solution()
result = solution.kthSmallest(root, k)
print(result)  # Output: 1

"""wlakthrough
1. Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
2. We define a TreeNode class to represent each node in the binary tree.
3. We create a Solution class with a method buildTree that takes the preorder and inorder lists as input.
4. We initialize a dummy head node and set curr to point to it. We also initialize indices i and j to 0, and n to the length of the preorder list.
5. We use a while loop to iterate through the preorder and inorder lists until we have processed all elements.
6. Inside the loop, we create a new node with the current value from the preorder list and attach it to the right of the current node. We then move curr to this new node and increment i.
7. We then enter another while loop to create left children for the current node until we reach the value that matches the current value in the inorder list.
8. After processing the left children, we increment j and enter another while loop to backtrack through the tree until we find a node whose right child matches the current value in the inorder list.
9. Finally, we return the right child of the dummy head node, which is the root
of the constructed binary tree.
10. The example usage demonstrates how to use the buildTree method to construct a binary tree from given preorder and inorder lists."""