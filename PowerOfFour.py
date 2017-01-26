#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given an integer (signed 32 bits),
write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""


def power_of_four(n):
    if n == 4:
        return 'true'
    if n % 4 == 0:
        return power_of_four(n/4)
    else:
        return 'false'

if __name__ == '__main__':
    n = 3
    print power_of_four(n)