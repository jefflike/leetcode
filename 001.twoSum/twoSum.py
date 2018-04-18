'''
__title__ = 'tes.py'
__author__ = 'Jeffd'
__time__ = '4/18/18 8:32 PM'
'''
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         i = 0
#         while i < len(nums):
#             j = i + 1
#             while j < len(nums):
#                 if nums[i]+nums[j] == target:
#                     return [i, j]
#                 j += 1
#             i += 1
#
#
# s = Solution()
# print(s.twoSum(nums=[2, 7, 11, 15], target=26))


# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         i = 0
#         while i < len(nums):
#             j = 0
#             while j < len(nums):
#                 if i != j and nums[i] + nums[j] == target:
#                     return [i, j]
#                 j += 1
#             i += 1
#
#
# s = Solution()
# print(s.twoSum(nums=[2, 7, 11, 15], target=26))


# class Solution:
#     '''
#
#     '''
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         new_dict = {i: nums[i] for i in range(len(nums))}
#         for i in new_dict:
#             if target - new_dict[i] in nums:
#                 for n in new_dict:
#                     if n != i and new_dict[n] == target - new_dict[i]:
#                         return [i, n]
#
#
# s = Solution()
# print(s.twoSum(nums=[2, 7, 11, 15], target=26))


class Solution:
    '''
        leetcode高分
    '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

s = Solution()
print(s.twoSum(nums=[2, 7, 11, 15], target=26))
