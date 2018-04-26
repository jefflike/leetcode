'''
__title__ = 'Merge Two Sorted Lists.py'
__author__ = 'Jeffd'
__time__ = '4/26/18 8:54 PM'
'''
'''
    tips:
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         数组不是列表
#         """
#         new_list = l1 + l2
#         return sorted(new_list)


class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b


s = Solution()
# print(s.mergeTwoLists([1, 2, 4], [1, 3, 4])) # 不是列表