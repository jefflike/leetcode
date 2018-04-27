'''
__title__ = 'Max Consecutive Ones.py'
__author__ = 'Jeffd'
__time__ = '4/27/18 10:52 PM'
'''
'''
    tips:
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''


# class Solution:
#     def findMaxConsecutiveOnes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         100ms
#         """
#         my_str = ''.join([str(i) for i in nums])
#         my_list = my_str.split('0')
#         my_len = len(my_list[0])
#         for i in  my_list:
#             if len(i)>my_len:
#                 my_len = len(i)
#         return my_len


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        68ms
        """
        count = 0
        ans = []
        for num in nums:
            if num == 1:
                count += 1
            else:
                ans.append(count)
                count = 0
        ans.append(count)
        return max(ans)


s = Solution()
print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))