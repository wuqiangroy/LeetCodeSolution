#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Write a function that takes an unsigned integer and
returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation
00000000000000000000000000001011, so the function should return 3.
"""


class Solution(object):

    def __init__(self, num):
        self.num = int(num)

    def number_of_bit(self):
        binary_num = bin(self.num)
        res = list(binary_num).count('1')
        return res

if __name__ == '__main__':
    num = 6
    s = Solution(num)
    print s.number_of_bit()

