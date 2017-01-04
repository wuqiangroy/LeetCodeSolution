#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

"""


class Solution(object):

    def __init__(self, num):
        self.num = list(num)
        self.num.sort()

    def missing_number(self):
        lst = []
        for n in range(len(self.num)-1):
            if self.num[n+1] - self.num[n] != 1:
                for x in range(self.num[n]+1, self.num[n+1]):
                    lst.append(x)
        return lst


class Solution2(object):
    def __init__(self, num):
        self.num = list(num)
        self.num.sort()

    def missing_number(self):
        lst = [x for x in range(self.num[0], self.num[-1]+1)]
        lst2 = []
        for i in lst:
            if i not in self.num:
                lst2.append(i)
        return lst2

num = [0, 1, 3, 4, 7]

s = Solution(num)
print s.missing_number()

s2 = Solution2(num)
print s2.missing_number()





