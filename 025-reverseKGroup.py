# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            # 1. Kiểm tra còn đủ k node không
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # không đủ k node -> dừng

            group_next = kth.next

            # 2. Đảo ngược nhóm k node
            prev = group_next
            cur = prev_group.next

            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            # 3. Nối lại
            tmp = prev_group.next  # đây sẽ là đuôi sau khi đảo
            prev_group.next = kth
            prev_group = tmp
        
        