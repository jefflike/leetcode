'''
__title__ = 'Number Complement.py'
__author__ = 'Jeffd'
__time__ = '4/20/18 9:58 PM'
'''
'''
    tips:
    Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
'''


# class Solution:
#     def findComplement(self, num):
#         """
#           36ms
#         :type num: int
#         :rtype: int
#         5 101 010 2
#         5 0101 1010 << 0100
#         1 0001 1110
#         """
#         # print(~str(bin(num)))
#         # new_num = str(num).lstrip('0')
#         # print(str(bin(~num))[3:])
#         new_list = []
#         for i in bin(num)[2:]:
#             if i == '0':
#                 i = '1'
#             else:
#                 i = '0'
#             new_list.append(i)
#         return int(''.join(new_list), 2)
#
#         # print(bin(num)) # 0b101 str
#         # print(int(bin(~num), 2)>>1)
#         # print(~num)
#
# s = Solution()
# print(s.findComplement(5))
# # s.findComplement(5)


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        32ms
        num = 5 101
        1 001 << 1 010 2
        2 << 1 100 4
        4 << 1 1000 8
        7 ^ 5 0111 ^ 0101 010 2

        """
        i = 1
        while i <= num:
            # 乘2直到大于num
            i = i << 1
        return (i - 1) ^ num