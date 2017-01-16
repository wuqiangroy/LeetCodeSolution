#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
"""


class Solution(object):

    def rotate_array(self, lst, n, k):

        if len(lst) != n:
            return "invalid length of list!"
        elif k > n:
            return "Wrong rotate!"
        last_lst, head_lst = lst[:k+1], lst[n-k:]
        res = head_lst+last_lst
        return res

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n, k = 9, 4
    s = Solution()
    print s.rotate_array(lst, n, k)
