#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 目前bug：重复没有按照list嵌套list方式return
# 2017.1.8 18:40
"""
Given an array S of n integers,
are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
import copy


class Solution(object):

    def __init__(self, lst):
        self.lst = list(lst)

    def Sum(self):
        n = 0
        res = []

        if len(self.lst) < 3:
            return False

        while n < len(self.lst) - 2:
            new_lst = copy.copy(self.lst)
            new_lst.pop(n)
            for i in range(n, len(self.lst)-2):
                new_lst.pop(0)
                if -(self.lst[n] + self.lst[i+1]) in new_lst:
                    res += [self.lst[n], self.lst[i+1], -(self.lst[n] + self.lst[i+1])]

            n += 1
        return res

if __name__ == '__main__':
    lst = [-1, 0, 1, 2, -1, -4]
    s = Solution(lst)
    print s.Sum()



