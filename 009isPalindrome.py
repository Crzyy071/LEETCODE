class Solution(object):
    def isPalindrome(self, x):
       # Số âm không thể là số đối xứng
        if x < 0:
            return False

        s = str(x)          # Đổi số thành chuỗi
        return s == s[::-1] # So sánh chuỗi với chuỗi đảo ngược