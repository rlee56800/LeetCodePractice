'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
'''

#ALMOST WORKS

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
            
        
