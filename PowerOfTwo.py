#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given an integer, write a function to determine if it is a power of two.
"""


def power_of_two(num):
    if num < 0:
        return 'false'
    flag = True
    while flag:
        if int(num**0.5) == num**0.5:
            flag = False
        else:
            return 'false'
    return 'true'

if __name__ == '__main__':
    num = 64
    print power_of_two(num)
