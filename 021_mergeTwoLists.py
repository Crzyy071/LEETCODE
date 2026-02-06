# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Tạo 1 node giả (dummy) để làm đầu danh sách kết quả
        dummy = ListNode(0)

        # cur (current) là con trỏ dùng để xây dựng danh sách mới
        cur = dummy

        # Khi cả hai list còn phần tử
        while list1 and list2:
            # So sánh giá trị 2 node hiện tại
            if list1.val < list2.val:
                # Nối node nhỏ hơn vào danh sách kết quả
                cur.next = list1
                # Di chuyển list1 sang node tiếp theo
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            # Di chuyển con trỏ cur sang node vừa nối
            cur = cur.next

        # Sau vòng lặp, một trong hai list có thể còn dư
        # Nối phần còn lại vào cuối danh sách kết quả
        cur.next = list1 or list2

        # Trả về danh sách kết quả (bỏ qua node dummy)
        return dummy.next
        