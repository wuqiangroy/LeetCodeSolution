#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given an array of integers,
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import copy
# 1


class Solution(object):

    def __init__(self, lst, target):
        self.lst = list(lst)
        self.lst.sort()
        self.target = int(target)

    def TwoSum(self):
        for n1 in range(len(self.lst)-1):
            for n2 in range(n1+1, len(self.lst)):
                if self.lst[n1] + self.lst[n2] == self.target:
                    return [n1, n2]


lst = [1, 3, 5, 6, 7, 8, 9]
target = 11
s = Solution(lst, target)
print s.TwoSum()

# 2


class Solution2(object):

    def __init__(self, lst, target):
        self.lst = list(lst)
        self.lst.sort()
        self.target = int(target)

    def TwoSum(self):
        n = 0
        while n < len(self.lst):
            new_lst = copy.copy(self.lst)
            new_lst.pop(n)
            num = self.target - self.lst[n]
            if num in new_lst:
                return [n, new_lst.index(num)+1]
                # 确定后者肯定大于前者，因为n是从第0位开始找，没找到才会越来越大
            n += 1

s2 = Solution2(lst, target)
print s2.TwoSum()

