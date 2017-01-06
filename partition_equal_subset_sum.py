#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that
the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

"""

import copy


class Solution(object):

    def __init__(self, lst):
        self.lst = list(lst)

    def CanPartition(self):
        i = 0
        while i < len(self.lst):
            new_lst = copy.copy(self.lst)
            new_lst.pop(i)
            total = 0
            for n in new_lst:
                total += n
            if total == self.lst[i]:
                return new_lst, [self.lst[i]]
            i += 1
        return 'false'

lst = [1, 3, 5, 6, 15]
s = Solution(lst)
print s.CanPartition()



