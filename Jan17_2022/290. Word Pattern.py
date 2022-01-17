'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        terms = {}
        s_split = s.split()
        
        if len(pattern) != len(s_split):
            return False
        
        if len(set(pattern)) != len(set(s_split)):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in terms:
                if terms[pattern[i]] != s_split[i]:
                    return False
            else:
                terms[pattern[i]] = s_split[i]
                
        return True
