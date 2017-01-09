#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given an array of integers sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution(object):

    def __init__(self, lst, target):
        self.lst = sorted(list(lst))
        self.target = int(target)

    def search_range(self):
        if self.target not in self.lst:
            return [-1, -1]
        else:
            n = 0
            while n < len(self.lst) - 1:
                if self.lst[n] == self.target < self.lst[n + 1]:
                    return [self.lst.index(self.target), n]
                n += 1

if __name__ == '__main__':
    lst = [1, 3, 3, 4, 4, 4, 7, 7, 8, 9, 11]
    target = 22
    s = Solution(lst, target)
    print s.search_range()

