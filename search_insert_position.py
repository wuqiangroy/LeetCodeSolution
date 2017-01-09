#!/usr/bin/env python
# _*_ coding:utf-8 _*_

""""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""


class Solution(object):

    def __init__(self, lst, target):
        self.lst = list(lst)
        self.target = int(target)

    def search_insert_position(self):
        if self.target in self.lst:
            return self.lst.index(self.target)
        elif self.target < self.lst[0]:
            return '0'
        elif self.target > self.lst[-1]:
                return len(self.lst)

        else:
            n = 0
            while n < len(self.lst)-1:
                if self.lst[n] < self.target < self.lst[n+1]:
                    return n+1
                n += 1

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 10, 23]
    target = 0
    s = Solution(lst, target)
    print s.search_insert_position()
