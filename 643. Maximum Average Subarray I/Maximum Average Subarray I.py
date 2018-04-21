'''
__title__ = 'Maximum Average Subarray I.py'
__author__ = 'Jeffd'
__time__ = '4/21/18 9:36 PM'
'''
'''
    tips: 
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
'''
'''
    ask:
    由于这道题子数组的长度k是确定的，所以我们其实没有必要建立整个累加数组，而是先算出前k个数字的和，然后就像维护一个滑动窗口一样，将窗口向右移动一位，
    即加上一个右边的数字，减去一个左边的数字，就等同于加上右边数字减去左边数字的差值，然后每次更新结果res即可
    千万不要遍历相加
'''


# class Solution:
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#
#         [1,12,-5,-6,50,3], k = 4
#         """
#         result = sorted(sum(nums[sumk:sumk+k]) for sumk in range(len(nums)) if sumk < len(nums)-k+1)[-1:]
#         max_avg = result[0] / k
#
#         return max_avg


# class Solution:
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#
#         [1,12,-5,-6,50,3], k = 4
#         """
#         result = max({sum(nums[sumk:sumk+k]) for sumk in range(len(nums)) if sumk < len(nums)-k+1})
#
#         return result/k


# class Solution:
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#
#         [1,12,-5,-6,50,3], k = 4
#         """
#         result = [sum(nums[sumk:sumk+k]) for sumk in range(len(nums)) if sumk < len(nums)-k+1]
#         max_result = result[0]
#         for i in result:
#             if i > max_result:
#                 max_result = i
#
#         return max_result/k


# class Solution:
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#
#         [1,12,-5,-6,50,3], k = 4
#         nums=[3, 3, 4, 3, 0], k=3
#         """
#         max_value = sum(nums[:k])
#         for sumk in range(len(nums)-k+1):
#             sum_value = sum(nums[sumk:sumk + k])
#             if sum_value > max_value:
#                 max_value = sum_value
#
#         max_result = max_value/k
#
#         return max_result


# class Solution:
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#         Runtime: 212 ms
#         [1,12,-5,-6,50,3], k = 4
#         nums=[3, 3, 4, 3, 0], k=3
#         """
#         max_value = sum(nums[:k])
#         my_set = {max_value}
#         for sumk in range(1, len(nums)-k+1):
#             # sum_value = sum(nums[sumk:sumk + k])
#             max_value = max_value+nums[sumk + k - 1]-nums[sumk -1]
#             my_set.add(max_value)
#             # if sum_value > max_value:
#             #     max_value = sum_value
#         max_value = max(my_set)
#
#         max_result = max_value/k
#
#         return max_result

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float

        leetcode 144 ms
        """
        _sum = sum(nums[:k])
        maxsum = _sum
        for i in range(k, len(nums)):
            _sum = _sum - nums[i-k] + nums[i]
            if _sum > maxsum:
                maxsum = _sum
        return maxsum/k


s = Solution()
print(s.findMaxAverage([1, 12, -5, -6, 50, 3, 4], 4))
print(s.findMaxAverage([5], 1))
# print(s.findMaxAverage(nums=[3, 3, 4, 3, 0], k=3))