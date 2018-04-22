'''
__title__ = 'Reverse Integer.py'
__author__ = 'Jeffd'
__time__ = '4/22/18 9:00 PM'
'''
'''
    tips: 
    Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
'''


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            result1 = int(''.join(reversed(str(x))))
            return 0 if result1 > (2**31-1) else result1
        else:
            result2 = int('-' + ''.join(reversed(str(abs(x)))))
            return 0 if result2 < (-2**31) else result2


s = Solution()
print(s.reverse(-123))
print(s.reverse(1534236469))
print(2**31)


# class Solution:
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         leetcode 52ms
#         """
#         if x < 0:
#             y = -1 * int(str(-x)[::-1])
#         else:
#             y = int(str(x)[::-1])
#
#         if y > 2 ** 31 or y < -2 ** 31:
#             y = 0
#         return y


# class Solution:
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         leetcode 60ms
#         """
#         flag = x < 0
#         p = x
#         if flag == True:
#             p = -1 * x
#
#         digit = []
#         while p != 0:
#             digit.append(p % 10)
#             p = p // 10
#
#         n = 0
#         for i in digit:
#             n = n * 10 + i
#
#         if -2 ** 31 <= n <= 2 ** 31 - 1:
#             return n if flag == False else -1 * n
#
#         return 0