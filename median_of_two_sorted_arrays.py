#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution():
    def FindMiddianSortedArrays(self, num1, num2):
        new_list = sorted(num1 + num2)
        if len(new_list) % 2 == 0:
            res = float(new_list[len(new_list)/2-1]+new_list[len(new_list)/2]) / 2
        else:
            res = float(new_list[(len(new_list)+1)/2-1])
        return res

num1 = [1, 5, 7, 10, 11, 44]
num2 = [2, 6, 8, 13]
s = Solution()
print s.FindMiddianSortedArrays(num1, num2)
