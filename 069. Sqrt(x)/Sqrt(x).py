'''
__title__ = 'Sqrt(x).py'
__author__ = 'Jeffd'
__time__ = '4/20/18 9:14 PM'
'''


'''
    python写这个毫无意义
    tips: Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''


import math


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))


s = Solution()
print(s.mySqrt(8))


class Solution:
    '''
    56ms
    '''
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int((x ** (1/2)))