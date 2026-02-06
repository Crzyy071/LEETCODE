class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)

        # 1. Tìm pivot
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. Nếu có pivot, tìm số lớn hơn gần nhất bên phải để swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 3. Reverse đoạn sau pivot
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1