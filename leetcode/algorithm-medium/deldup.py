# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        curr=head.next
        prev=head
        while(curr):
            if curr.val==prev.val:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return head
            
