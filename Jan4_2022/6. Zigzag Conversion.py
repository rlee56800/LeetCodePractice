'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
        
        zig = [''] * numRows
        
        count = 0
        down = False
        for char in s:
            zig[count] += char
            if count==0 or count==numRows-1:
                down = not down
            count = count + 1 if down else count - 1
        
        ret_str = ""
        for zag in zig:
            ret_str += zag
        
        return ret_str
            

'''
# OLD
# This would've been cool if it worked
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        largest = (numRows - 1) * 2
        alt = current = largest
        ret_str = ""
        
        for i in range(numRows):
            counter = i
            alternate = 0
            while counter < len(s):
                ret_str += s[counter]
                if alternate%2 == 0:
                    counter += current
                    alternate = 1
                else:
                    counter += alt
                    alternate = 0
            
            current = current-2 if current != 2 else largest
            alt = alt+2 if alt != largest else 2
        
        return ret_str
'''
            
        
