'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        passed = {} # dictionary of passed values
        
        for index, value in enumerate(nums): # returns tuple of index and value
            diff = target - value # only 2 numbers used (not scalable :< )
            if diff in passed: # use difference as key
                return [passed[diff], index]
            else:
                passed[value] = index # new dictionary entry
        return []
