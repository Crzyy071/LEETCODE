class Solution(object):
    def twoSum(self, nums, target):
        seen = {}                  # lưu: số -> index

        for i, n in enumerate(nums):
            need = target - n      # số còn thiếu
            if need in seen:       # nếu đã gặp số cần tìm
                return [seen[need], i]
            seen[n] = i            # lưu số hiện tại