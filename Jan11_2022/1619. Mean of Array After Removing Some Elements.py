'''
Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.

Answers within 10-5 of the actual answer will be considered accepted.
''' 

import math
class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        sorted = arr.sort()
        
        trim = int(math.ceil(len(arr) * 0.05))
        
        sum = 0
        for i in range(trim, len(arr) - trim):
            sum += arr[i]
        
        return sum / (len(arr) - (2*trim))
