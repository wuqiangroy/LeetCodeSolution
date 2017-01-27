#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given an integer (signed 32 bits),
write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""


def power_of_four(num):
    if num < 0:
        return 'false'
    if int(num**0.25) == num**0.25:
        return 'true'
    else:
        return 'false'


if __name__ == '__main__':
    n = 16
    print power_of_four(n)
