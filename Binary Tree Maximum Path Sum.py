"""A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
    
#example usage
solution = Solution()   
root = [1,2,3]
print(solution.maxPathSum(root))  # Output: 6
inorder = [9,3,15,20,7]
print(solution.buildTree(preorder, inorder))  # Output: [3,9,20,null,null,15,7]
inorder = [9,3,15,20,7]
print(solution.buildTree(preorder, inorder))  # Output: [3,9,20,null,null,15,7]

"""walkthrough
1. We define a helper function `dfs` that computes the maximum path sum for each subtree rooted at the given node.
2. For each node, we recursively compute the maximum path sums of its left and right subtrees.
3. We ignore negative path sums by taking the maximum of the computed sums and 0.
4. We update the global maximum path sum (`res[0]`) by considering the path that passes through the current node and both its left and right children.
5. Finally, we return the maximum path sum found during the traversal.
6. The overall time complexity is O(N), where N is the number of nodes in the tree, since we visit each node exactly once.
7. The space complexity is O(H), where H is the height of the tree, due to the recursion stack."""