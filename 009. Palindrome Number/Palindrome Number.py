'''
__title__ = 'Palindrome Number.py'
__author__ = 'Jeffd'
__time__ = '4/23/18 10:57 PM'
'''
'''
    tips:
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''


# class Solution:
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x >= 0:
#             if x // 10 == 0:
#                 return True
#             else:
#                 my_list = []
#                 i = 0
#                 while x // 10 > 0:
#                     v = x % 10
#                     x = x // 10
#                     my_list.append(v)
#                     i += 1
#                 my_list.append(x)
#                 for count in range(i):
#                     if my_list[count] != my_list[-(count+1)]:
#                         return False
#                 return True
#
#         else:
#             return False


# class Solution:
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         340ms
#         """
#         if x >= 0:
#             my_list = []
#             i = 0
#             while x // 10 > 0:
#                 v = x % 10
#                 x = x // 10
#                 my_list.append(v)
#                 i += 1
#             my_list.append(x)
#             for count in range(i):
#                 if my_list[count] != my_list[-(count+1)]:
#                     return False
#             return True
#
#         else:
#             return False


# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         312ms
#         通过比较反转整数和原整数是否相等来判断回文。
#         """
#         if x < 0:
#             return False
#
#         tmp = x
#         y = 0
#         while tmp:
#             y = y*10 + tmp%10
#             tmp = tmp//10
#         return y == x


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        若不想生成反转数字，可考虑将原整数的各个数字分离，逐个比较最前最后的数字是否相等。
        332ms
        """
        if x < 0:
            return False

        digits = 1
        while x/digits >= 10:
            digits *= 10

        while digits > 1:
            right = x%10
            left = x//digits
            if left != right:
                return False
            x = (x%digits) // 10
            digits //= 100
        return True


s = Solution()
print(s.isPalindrome(12321))