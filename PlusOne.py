#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given a non-negative integer represented as a non-empty array of digits,
plus one to the integer.

You may assume the integer do not contain any leading zero,
except the number 0 itself.

The digits are stored such that the
most significant digit is at the head of the list.
"""


class Solution(object):

    def __init__(self, lst, num):
        self.lst = list(lst)
        self.lst.sort(lambda x, y: y-x)
        self.num = int(num)

    def plus_one(self):
        if len(self.lst) == 0:
            self.lst.insert(0, self.num)
            return self.lst
        n = 0
        while n < len(self.lst):
            if self.num > self.lst[n]:
                self.lst.insert(n, self.num)
                return self.lst
            n += 1


class Solution2(object):

    def __init__(self, lst, num):
        self.lst = list(lst)
        self.num = int(num)

    def plus_one(self):
        self.lst.append(self.num)
        self.lst.sort(lambda x, y: y-x)
        return self.lst

if __name__ == '__main__':
    lst = []
    num = 8
    s = Solution(lst, num)
    s2 = Solution2(lst, num)
    print s.plus_one()
    print s2.plus_one()

