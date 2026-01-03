"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order."""

#answe
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
        
#example usage
# Creating two sorted linked lists for demonstration:   
list1 = ListNode(1)  
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
sol = Solution()
merged_head = sol.mergeTwoLists(list1, list2)
# Printing the merged linked list
current = merged_head
while current:
    print(current.val, end=" -> " if current.next else "")
    current = current.next
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

"""walkthrough
1. Initialize a dummy node to serve as the starting point of the merged list.
2. Use a pointer `node` to track the end of the merged list as we build it.
3. Iterate through both lists, comparing the current nodes of each list.    
4. Append the smaller node to the merged list and move the corresponding pointer forward.
5. Once we reach the end of one list, append the remaining nodes of the other list.
6. Return the merged list, which starts from `dummy.next`.
7. This approach ensures that the merged list is sorted as we only append the smaller node at each step."""