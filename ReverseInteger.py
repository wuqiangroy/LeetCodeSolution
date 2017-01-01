#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

"""

class ReverseInteger():
    def reverse_integer(self, num):
            num_list = list(str(abs(num)))
            num_list.reverse()
            new_num = int(''.join(num_list))
            if num > 0:
                return new_num
            else:
                return -new_num

ri = ReverseInteger()
print ri.reverse_integer(-5674)


