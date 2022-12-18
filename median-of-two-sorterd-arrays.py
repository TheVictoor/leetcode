class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()        
        if len(nums1) & 1 == 1:
            return nums1[len(nums1)//2]
        else:
            median = len(nums1) // 2
            return (nums1[median] + nums1[median-1]) / 2


print(Solution().findMedianSortedArrays([1,3,4], [2,7]))