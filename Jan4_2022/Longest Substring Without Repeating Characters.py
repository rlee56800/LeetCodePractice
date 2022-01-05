'''Given a string s, find the length of the longest substring without repeating characters.'''

# doesn't work w input s = " "

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        letters = ""
        totals = 0

        for char in s:
            if char in letters:
                if len(letters) > totals:
                    totals = len(letters)
                letters = ""
            letters+= char
        
        return totals
