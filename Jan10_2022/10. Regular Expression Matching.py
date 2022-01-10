class Solution(object):
    def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    
    p_index = 0
    for i in range(len(s)):
        if p_index >= len(p):
            return False
        if p[p_index] == '*':
            p_index += -1
        if p[p_index] != '.' and s[i] != p[p_index]:
            return False
        # else s[i] == p[p_index]; keep going
        p_index += 1
    
    return True
            
            
# doesn't work for print(isMatch("aab", "c*a*b"))
