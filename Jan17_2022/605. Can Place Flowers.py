'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        potential = 0
        
        for i in range(0, len(flowerbed)):
            if (not flowerbed[i]) and (i == 0 or not flowerbed[i-1]) and (i == len(flowerbed)-1 or not flowerbed[i+1]):
                flowerbed[i] = 1
                potential += 1 
        
        return potential >= n
