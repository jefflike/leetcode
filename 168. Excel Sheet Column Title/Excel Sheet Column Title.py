'''
__title__ = 'Excel Sheet Column Title.py'
__author__ = 'Jeffd'
__time__ = '4/28/18 7:48 PM'
'''
'''
    tips:
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''


# class Solution:
#     def convertToTitle(self, n):
#         """
#         :type n: int
#         :rtype: str
#         """
#         # print(ord('A'))
#         if n < 27:
#             return chr(n+64)
#         else:
#             return chr(n//26+64)+chr(n%26+64)

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        32ms
        """
        result = ''
        distance = ord('A')

        while n > 0:
            y = (n-1) % 26
            n = (n-1) // 26
            s = chr(y+distance)
            result = ''.join((s, result))

        return result


s = Solution()
# print(s.convertToTitle(26))
print(s.convertToTitle(701))