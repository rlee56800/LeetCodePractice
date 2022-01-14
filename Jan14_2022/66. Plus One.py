'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr = digits
        arr[-1] += 1
        if arr[-1] == 10:
            if len(arr) == 1:
                return [1,0]
            arr = self.plusOne(arr[:-1])
            arr.append(0)
        return arr
            
