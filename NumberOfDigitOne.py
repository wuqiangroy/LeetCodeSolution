#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given an integer n, count the total number of digit 1 appearing in
all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""


class Solution(object):

    def digit_one(self, n):
        count = 0
        for i in range(n+1):
            count += list(str(i)).count('1')
        return count

if __name__ == '__main__':
    n = 15
    s = Solution()
    print s.digit_one(n)
