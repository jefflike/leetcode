'''
__title__ = 'Longest Common Prefix.py'
__author__ = 'Jeffd'
__time__ = '4/24/18 9:35 PM'
'''
'''
    tips:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''


# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         错误
#         """
#         mid_value = len(strs[0])//2
#         max_prefix = strs[0][:mid_value-1]
#         # print(max_prefix)
#         for i in strs:
#             if max_prefix in i:
#                 max_prefix = i[:mid_value+mid_value//2]
#             else:
#                 max_prefix = i[mid_value // 2]
#         return max_prefix


class Solution:
    # @return a string
    # 40ms
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        print(list(enumerate(zip(*strs))))
        # [(0, ('f', 'f', 'f')), (1, ('l', 'l', 'l')), (2, ('o', 'o', 'i')), (3, ('w', 'w', 'g'))]
        for i, letter_group in enumerate(zip(*strs)):
            # print(i)
            # print(letter_group)
            # 0
            # ('f', 'f', 'f')
            # 1
            # ('l', 'l', 'l')
            # 2
            # ('o', 'o', 'i')
            # fl

            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         36ms
#         """
#         strs = strs
#         import os
#         return os.path.commonprefix(strs)


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))