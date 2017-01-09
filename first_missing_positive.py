#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""


class Solution(object):

    def __init__(self, lst):
        self.lst = sorted(list(lst))

    def missing_number(self):
        n = 0
        while n < len(self.lst)-1:
            if self.lst[n+1]-1 != self.lst[n] and self.lst[n] >= 0:
                return self.lst[n]+1
            n += 1
        return self.lst[-1] + 1
if __name__ == '__main__':
    lst = [2, 4, 5, 1, 3]
    s = Solution(lst)
    print s.missing_number()


