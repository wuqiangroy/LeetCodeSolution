#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Given an array of integers, every element appears three times except for one,
which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""


class Solution(object):

    def __init__(self, lst):
        self.lst = sorted(list(lst))

    def single_number(self):
        n = 0
        while n < len(self.lst):
            if self.lst.count(self.lst[n]) == 3:
                n += 3
            else:
                return self.lst[n]

if __name__ == '__main__':
    lst = [2, 3, 4, 5, 4, 7, 3, 2, 4, 3, 2, 5, 5]
    s = Solution(lst)
    print s.single_number()
