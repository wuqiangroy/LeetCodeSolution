#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given an integer, write a function to determine if it is a power of two.
"""


def power_of_two(num):
    if num == 1:
        return 'true'
    if num % 2 == 0:
        return power_of_two(num/2)
    return 'false'

if __name__ == '__main__':
    num = 128
    print power_of_two(num)
