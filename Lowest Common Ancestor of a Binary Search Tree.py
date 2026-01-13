"""Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST."""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
            

#example usage
sorted_tree = TreeNode(6)
sorted_tree.left = TreeNode(2)  
sorted_tree.right = TreeNode(8)
sorted_tree.left.left = TreeNode(0)
sorted_tree.left.right = TreeNode(4)
sorted_tree.right.left = TreeNode(7)
sorted_tree.right.right = TreeNode(9)
sorted_tree.left.right.left = TreeNode(3)
sorted_tree.left.right.right = TreeNode(5)  
p = sorted_tree.left  
q = sorted_tree.right   
solution = Solution()
lca = solution.lowestCommonAncestor(sorted_tree, p, q)
print(f"The Lowest Common Ancestor of nodes {p.val} and {q.val} is: {lca.val}")

"""walkthrough
1. Start at the root of the BST.
2. Compare the values of nodes p and q with the value of the current node (cur).
3. If both p and q have values greater than cur, move to the right child of cur.
4. If both p and q have values less than cur, move to the left child of cur.
5. If neither of the above conditions is true, cur is the LCA of p and q, so return cur.    
6. The process continues until the LCA is found.
7. The time complexity is O(h), where h is the height of the tree, and the space complexity is O(1) since we are using only a constant amount of extra space."""