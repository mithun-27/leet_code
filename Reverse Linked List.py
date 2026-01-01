"""Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?"""

#answer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
#example usage
# Creating a linked list for demonstration: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)  
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
sol = Solution()
reversed_head = sol.reverseList(head)
# Printing the reversed linked list
current = reversed_head
while current:
    print(current.val, end=" -> " if current.next else "")
    current = current.next
# Output: 5 -> 4 -> 3 -> 2 -> 1

"""walkthrough
1. Initialize two pointers, `prev` as `None` and `curr` as the head of the linked list.
2. While `curr` is not `None`, do the following:
   a. Store the next node of `curr` in a temporary variable `temp`.
   b. Reverse the link by setting `curr.next` to `prev`.
   c. Move `prev` to `curr` and `curr` to `temp`.
3. Once the loop ends, `prev` will be the new head of the reversed linked list. Return `prev`.
Compare this snippet from Find%20Minimum%20in%20Rotated%20Sorted%20Array.py:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
"""