class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        merged = ListNode(-1)
        copy = merged
        while l1 and l2:
            if l1.val <= l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            merged = merged.next
        while l1:
            merged.next = l1
            l1 = l1.next
            merged = merged.next
        while l2:
            merged.next = l2
            l2 = l2.next
            merged = merged.next
        return copy.next
