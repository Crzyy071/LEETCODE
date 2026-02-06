# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        # fast đi trước n bước
        for _ in range(n):
            fast = fast.next

        # cùng đi cho tới khi fast tới cuối
        while fast.next:
            fast = fast.next
            slow = slow.next

        # xóa node
        slow.next = slow.next.next

        return dummy.next
        