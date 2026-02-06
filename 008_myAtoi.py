class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # 1. Bỏ khoảng trắng đầu
        while i < n and s[i] == ' ':
            i += 1

        # 2. Xét dấu
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Đọc số
        num = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # 4. Kiểm tra tràn trước khi nhân 10
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num

        