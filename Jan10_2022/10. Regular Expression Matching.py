class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_index = 0 # current character being viewed
#        star = False
           
        for i in range(len(s)):
            if p_index >= len(p): # more letters in s than open rules
                return False
            if p[p_index] == '*': # compare previous letter in p
                p_index += -1
            if p[p_index] != '.' and s[i] != p[p_index]:
                # not . and nor the same letter
                try: # in case p_index > len(p)
                    if p[p_index+1] != '*': # current letter appears 0 times
                        return False
                except:
                    return False
            p_index += 1

        return True


    # doesn't work for print(isMatch("mississippi", "mis*is*p*."))
