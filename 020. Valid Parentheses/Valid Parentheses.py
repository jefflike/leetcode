'''
__title__ = 'Valid Parentheses.py'
__author__ = 'Jeffd'
__time__ = '4/25/18 8:28 PM'
'''
'''
    tips:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = ['']
        parmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in parmap and parmap[c] == pars[len(pars)-1]:
                pars.pop()
            else:
                pars.append(c)
        return len(pars) == 1


s = Solution()
print(s.isValid('()[]{}'))
s.isValid('{[]}')
print(s.isValid('{[}{]}'))