'''
__title__ = 'Find All Numbers Disappeared in an Array.py'
__author__ = 'Jeffd'
__time__ = '4/29/18 8:14 PM'
'''
'''
    tips:
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''


# class Solution:
#     def findDisappearedNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         if nums == []:
#             return []
#         new_list = []
#         # max_nums = max(nums)
#         for i in range(1, len(nums)+1):
#             if i not in nums:
#                 new_list.append(i)
#         return new_list


# class Solution:
#     def findDisappearedNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         if nums == []:
#             return []
#         new_list = []
#         for i in range(1, len(nums)+1):
#             if i not in nums:
#                 new_list.append(i)
#         return new_list

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        164ms
        """
        return list(set(list(range(1, len(nums)+1)))-set(nums))


s = Solution()
print(s.findDisappearedNumbers([1, 1]))
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))