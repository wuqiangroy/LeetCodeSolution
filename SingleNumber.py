#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Given an array of integers,
every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""


class Solution(object):

    def __init__(self, num):
        self.num = list(num)

    def single_number(self):
        for n in self.num:
            if self.num.count(n) == 1:
                return self.num[n]
            n += 1

if __name__ == '__main__':
    num = [1, 1, 2, 3, 4, 5, 4, 6, 5, 3, 6]
    s = Solution(num)
    print s.single_number()


