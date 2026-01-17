"""Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 """
#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root

        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right

        return -1
#example usage
# Constructing the binary search tree [3,1,4,null,2]
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)   
k = 1
solution = Solution()
print(solution.kthSmallest(root, k))  # Output: 1

"""walkthrough
1. We define a class Solution with a method kthSmallest that takes the root of a binary search tree and an integer k as input.
2. We initialize a variable curr to the root of the tree.
3. We enter a while loop that continues as long as curr is not None.
4. Inside the loop, we check if curr has a left child.
   - If it does not have a left child, we decrement k by 1. If k becomes 0, we return the value of curr as it is the kth smallest element. We then move curr to its right child.
   - If curr has a left child, we find its inorder predecessor (the rightmost node in its left subtree). We do this by initializing a variable pred to curr.left and traversing to the rightmost node.
     - If pred.right is None, we set pred.right to curr (creating a temporary link) and move curr to its left child.
     - If pred.right is curr (indicating we've already visited the left subtree), we remove the temporary link by setting pred.right to None, decrement k by 1, and check if k is 0 to return curr.val. We then move curr to its right child.
5. If we exit the loop without returning, we return -1 as a fallback (though this should not happen given the problem constraints).
"""