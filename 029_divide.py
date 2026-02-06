class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # case overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # xác định dấu
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        a = abs(dividend)
        b = abs(divisor)

        res = 0
        while a >= b:
            temp = b
            multiple = 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            a -= temp
            res += multiple

        return sign * res

        