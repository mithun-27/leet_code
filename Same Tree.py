"""Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                nodeP = q1.popleft()
                nodeQ = q2.popleft()

                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False

                q1.append(nodeP.left)
                q1.append(nodeP.right)
                q2.append(nodeQ.left)
                q2.append(nodeQ.right)

        return True

#example usage
sol = Solution()
# Example 1
p1 = TreeNode(1)    
p1.left = TreeNode(2)
p1.right = TreeNode(3)
q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)
print(sol.isSameTree(p1, q1))  # Output: True
# Example 2 
p2 = TreeNode(1)
p2.left = TreeNode(2)
q2 = TreeNode(1)
q2.right = TreeNode(2)
print(sol.isSameTree(p2, q2))  # Output: False
# Example 3
p3 = TreeNode(1)
p3.left = TreeNode(2)
p3.right = TreeNode(1)
q3 = TreeNode(1)
q3.left = TreeNode(1)
q3.right = TreeNode(2)
print(sol.isSameTree(p3, q3))  # Output: False

"""walkthrough
1. We define a class Solution with a method isSameTree that takes two binary tree roots p and q as input.
2. We initialize two deques, q1 and q2, to perform level-order traversal on both trees.
3. We enter a while loop that continues as long as both deques are not empty.   
4. Inside the loop, we iterate through the nodes at the current level of both trees.
5. For each pair of nodes (nodeP from tree p and nodeQ from tree q):
   - If both nodes are None, we continue to the next iteration.
   - If one node is None or their values are not equal, we return False.
   - If the nodes are equal, we append their left and right children to the respective deques.
6. If we finish traversing both trees without finding any differences, we return True, indicating that the trees are the same.
   c. If the left child exists, push it onto the stack.
   d. If the right child exists, push it onto the stack.
"""