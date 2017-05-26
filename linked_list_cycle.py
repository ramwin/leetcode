# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        while True:
            head.checked = True
            head = head.next
            if head is None:
                return False
            if hasattr(head, 'checked'):
                return True
