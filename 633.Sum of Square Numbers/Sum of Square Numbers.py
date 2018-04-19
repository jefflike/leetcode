'''
__title__ = '633.Sum of Square Numbers.py'
__author__ = 'Jeffd'
__time__ = '4/19/18 9:31 PM'
'''
'''
    tips: 
    Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

    Example 1:
    Input: 5
    Output: True
    Explanation: 1 * 1 + 2 * 2 = 5
    
'''
# import math


# class Solution:
#     def judgeSquareSum(self, c):
#         """
#         :type c: int
#         :rtype: bool
#         """
#
#         # 13 2*2 + 3*3
#         # 0 0*0 + 0*0
#         # 2 1*1 + 1*1
#         max = math.sqrt(c)
#         print(max)
#         # if max * max == c:
#         #
#         #     return True
#         new_set = set()
#         for i in range(0, int(max)+1):
#             if i * i * 2 == c:
#                 return True
#             elif c - i * i in new_set:
#                 return True
#             else:
#                 new_set.add(i * i)
#         return False
#
#
# s = Solution()
# print(s.judgeSquareSum(1000000000))

# class Solution:
#     def judgeSquareSum(self, c):
#         """
#         :type c: int
#         :rtype: bool
#         """
#
#         # 13 2*2 + 3*3
#         # 0 0*0 + 0*0
#         # 2 1*1 + 1*1
#         max = c ** 0.5
#         new_set = set()
#         for i in range(0, int(max)+1):
#             if i * i * 2 == c:
#                 return True
#             elif c - i * i in new_set:
#                 return True
#             else:
#                 new_set.add(i * i)
#         return False


# s = Solution()
# print(s.judgeSquareSum(1000000000))


# class Solution:
#     def judgeSquareSum(self, c):
#         """
#         :type c: int
#         :rtype: bool
#         """
#
#         # 13 2*2 + 3*3
#         # 0 0*0 + 0*0
#         # 2 1*1 + 1*1
#         max = c ** 0.5
#         # new_set = set()
#         for i in range(0, int(max)+1):
#             print((c - i * i) ** 0.5)
#             if isinstance((c - i * i) ** 0.5, int):
#                 return True
#         return False
#
# s = Solution()
# # print(s.judgeSquareSum(1000000000))
# print(s.judgeSquareSum(0)) 丢失精度

import math


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        108ms
        """
        for num in range(int(math.sqrt(c//2)),int(math.sqrt(c))+1):
            residue = math.sqrt(c - num*num)
            if residue == int(residue):
                return True
        return False