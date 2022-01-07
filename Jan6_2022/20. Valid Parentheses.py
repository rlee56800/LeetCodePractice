'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        matching = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            if char in matching:
                stack.append(char)
            else:
                if len(stack) == 0 or matching[stack[-1]] != char:
                    return False
                else:
                    stack.pop()
        
        if not stack:
            return True
        else:
            return False
