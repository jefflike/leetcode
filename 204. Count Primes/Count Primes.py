'''
__title__ = 'Count Primes.py'
__author__ = 'Jeffd'
__time__ = '4/30/18 9:14 PM'
'''
'''
    tips:
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, n):
            if res[i] == True:
                for j in range(2, (n - 1) // i + 1):
                    res[i * j] = False
        return sum(res)


s = Solution()
print(s.countPrimes(10))