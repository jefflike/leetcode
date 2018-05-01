'''
__title__ = 'Maximum Product of Three Numbers.py'
__author__ = 'Jeffd'
__time__ = '5/1/18 8:26 PM'
'''
'''
    tips:
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''


# class Solution:
#     def maximumProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums)<3: return None
#         so=sorted(nums)
#         return max(so[-1]*so[-2]*so[-3],so[-1]*so[0]*so[1])


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0]*a[1]*a[2], a[0]*b[0]*b[1])

