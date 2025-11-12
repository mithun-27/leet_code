"""You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

 

Example 1:

Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Explanation:



Remove the nodes with values 1, 2, and 3.

Example 2:

Input: nums = [1], head = [1,2,1,2,1,2]

Output: [2,2,2]

Explanation:



Remove the nodes with value 1.

Example 3:

Input: nums = [5], head = [1,2,3,4]

Output: [1,2,3,4]

Explanation:



No node has value 5.

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
All elements in nums are unique.
The number of nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
The input is generated such that there is at least one node in the linked list that has a value not present in nums."""

#answer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List, Optional

class Solution:
    def modifiedList(self, nums: List[int], head: Optional['ListNode']) -> Optional['ListNode']:
        remove = set(nums)
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr:
            if curr.val in remove:
                prev.next = curr.next   # delete curr
            else:
                prev = curr             # keep curr
            curr = curr.next

        return dummy.next

# Example usage:
sol = Solution()
sol.modifiedList([1,2,3], ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))  # Output: [4,5]
sol.modifiedList([1], ListNode(1, ListNode(2, ListNode(1, ListNode(2, ListNode(1, ListNode(2)))))))  # Output: [2,2,2]
sol.modifiedList([5], ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))  # Output: [1,2,3,4]

"""walkthrough:
1. We first convert the list nums into a set called remove for O(1) average-time complexity lookups.
2. We create a dummy node that points to the head of the linked list. This helps handle edge cases where the head itself needs to be removed.
3. We initialize two pointers, prev and curr. prev starts at the dummy node, and curr starts at the head of the linked list.
4. We iterate through the linked list using the curr pointer:
   - If the value of the current node (curr.val) is in the remove set, we skip this node by setting prev.next to curr.next.
   - If the value is not in the remove set, we move the prev pointer to curr.
   - In both cases, we move the curr pointer to the next node in the list.
5. Finally, we return dummy.next, which points to the head of the modified linked list."""
