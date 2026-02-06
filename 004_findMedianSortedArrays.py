class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num=nums1+nums2
        num.sort()
        dodai=len(num)
        if (dodai % 2 ==1):
            return num[dodai // 2]
        else:
            s1 = num[dodai // 2 - 1]
            s2 = num[dodai// 2]
            return (s1+s2)/2.0