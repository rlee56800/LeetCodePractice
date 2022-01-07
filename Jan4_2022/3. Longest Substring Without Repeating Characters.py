'''Given a string s, find the length of the longest substring without repeating characters.'''

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
                letters = letters[letters.index(char)+1:]
            letters+= char
        
        return max(totals, len(letters))       
