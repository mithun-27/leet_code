"""Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return "$#"

        return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))

    def z_function(self, s: str) -> list:
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return z

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized_root = self.serialize(root)
        serialized_subRoot = self.serialize(subRoot)
        combined = serialized_subRoot + "|" + serialized_root

        z_values = self.z_function(combined)
        sub_len = len(serialized_subRoot)

        for i in range(sub_len + 1, len(combined)):
            if z_values[i] == sub_len:
                return True
        return False

#example usage
sol = Solution()
# Example 1
root1 = TreeNode(3)
root1.left = TreeNode(4)
root1.right = TreeNode(5)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(2)
subRoot1 = TreeNode(4)
subRoot1.left = TreeNode(1)
subRoot1.right = TreeNode(2)
print(sol.isSubtree(root1, subRoot1))  # Output: True

# Example 2
root2 = TreeNode(3)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(2)
root2.left.right.left = TreeNode(0)
subRoot2 = TreeNode(4)
subRoot2.left = TreeNode(1)
subRoot2.right = TreeNode(2)
print(sol.isSubtree(root2, subRoot2))  # Output: False

"""walkthrough
1. **Serialization**: The `serialize` method converts a binary tree into a string representation using pre-order traversal. It uses "$" to denote node values and "#" to denote null nodes. This ensures that the structure of the tree is preserved in the string.
2. **Z-Function**: The `z_function` method computes the Z-array for a given string. The Z-array at position `i` indicates the length of the longest substring starting from `i` that matches a prefix of the string. This is useful for pattern matching.   
3. **Subtree Check**: The `isSubtree` method first serializes both the main tree (`root`) and the subtree (`subRoot`). It then combines these two serialized strings with a unique separator ("|") to avoid false matches. The Z-function is computed on this combined string.  
4. **Pattern Matching**: The method iterates through the Z-array starting from the index just after the separator. If any value in the Z-array equals the length of the serialized `subRoot`, it indicates that `subRoot` is a subtree of `root`, and the method returns `True`. If no such match is found, it returns `False`.     
    - If both nodes are valid and their values are equal, we enqueue their left and right children for further comparison.
5. If we complete the traversal without finding any discrepancies, we return True, indicating that the two trees are identical.
"""