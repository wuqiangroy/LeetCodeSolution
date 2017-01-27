#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""


def power_of_three(num):
    num = abs(num)
    n = float(1) / 3
    if int(num**n) == num**n:
        return 'true'
    else:
        return 'false'

if __name__ == '__main__':
    num = -8
    print power_of_three(num)
