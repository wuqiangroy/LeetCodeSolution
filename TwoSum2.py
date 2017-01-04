#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=2, index2=7

"""


class Solution(object):

    def __init__(self, num, target):
        self.num = list(num)
        self.num.sort()
        self.target = int(target)

    def two_sum(self):
        for n1 in range(len(self.num)):
            for n2 in range(n1+1, len(self.num)):
                if self.num[n1] + self.num[n2] == self.target and \
                        self.num[n1] <= self.num[n2]:
                    return "index{0}={1}, index{2}={3}".format(
                        n1+1, self.num[n1], n2+1, self.num[n2])

num = [1, 3, 6, 9, 21, 33, 44, 55]
target = 15
s = Solution(num, target)
print s.two_sum()


