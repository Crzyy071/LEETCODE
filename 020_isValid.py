class Solution(object):
    def isValid(self, s):
        stack = []
        mp = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in mp:  # là ngoặc đóng
                if not stack or stack[-1] != mp[ch]:
                    return False
                stack.pop()
            else:  # là ngoặc mở
                stack.append(ch)

        return len(stack) == 0
    