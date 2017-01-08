#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given a digit string
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):

    def __init__(self, num):
        self.num = str(num)

    def phone_number(self):
        phone_number = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pgrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        i = 0
        li = []
        while i < len(self.num):
            li.append(phone_number[self.num[i]])
            i += 1
        res = []
        for n in li[0]:
            for j in li[1]:
                res.append(n+j)

        return res

if __name__ == '__main__':
    " only two numbers"
    num = '34'
    s = Solution(num)
    print s.phone_number()

