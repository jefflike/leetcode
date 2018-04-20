'''
__title__ = 'Add Binary.py'
__author__ = 'Jeffd'
__time__ = '4/20/18 9:39 PM'
'''
'''
    tips: 
    Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution:
    def addBinary(self, a, b):
        """
        44 ms
        first 36ms也是这个答案
        :type a: str
        :type b: str
        :rtype: str
        """
        ex_a = bin(int(a, 2) + int(b, 2))
        return str(ex_a)[2:]


s = Solution()
print(s.addBinary('1010', '1011'))
