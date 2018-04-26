'''
__title__ = 'Power of Four.py'
__author__ = 'Jeffd'
__time__ = '4/26/18 9:14 PM'
'''
'''
    tips:
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
'''


import math


# class Solution:
#     def isPowerOfFour(self, num):
#         """
#         :type num: int
#         :rtyp
#         """
#         if num <= 0:
#             return False
#         a = math.log(abs(num), 4)
#         return a.is_integer()


class Solution:
    def isPowerOfFour(self, n):
        test = 1
        while test < n:
            test = test << 2
        return test == n


s = Solution()
s.isPowerOfFour(1)