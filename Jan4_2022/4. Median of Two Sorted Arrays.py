'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums = nums1 + nums2
        nums.sort()

        nums_size = len(nums)
        if nums_size%2 == 0:
            lesser = int(nums_size/2)
            return (nums[lesser] + nums[lesser-1])/2.000
        else:
            return nums[nums_size//2]
        
