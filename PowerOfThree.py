#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""


def power_of_three(num):
    if num == 1:
        return 'true'
    if num % 3 == 0:
        return power_of_three(num/3)
    else:
        return 'false'


if __name__ == '__main__':
    num = 28
    print power_of_three(num)