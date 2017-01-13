#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Given an unsorted array of integers,
find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


class Solution(object):

    def __init__(self, lst):
        self.lst = sorted(list(lst))

    def longest_number_list(self):
        n, count, res = 0, 2, 0
        res_list = []
        while n < len(self.lst)-1:
            if self.lst[n+1] - self.lst[n] == 1:
                res = count
                count += 1
                res_list.append(res)
            else:
                count = 1
            n += 1
        return max(res_list)

if __name__ == '__main__':
    lst = [200, 1, 300, 2, 43, 3, 45, 4, 46, 5]
    s = Solution(lst)
    print s.longest_number_list()
