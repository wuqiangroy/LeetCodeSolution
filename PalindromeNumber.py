#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Determine whether an integer is a palindrome. Do this without extra space.
确定一个数是否为回文数，不适用额外空间
"""


class Solution(object):

    def __init__(self, num):
        self.num = str(num)

    def palindrome_number(self):
        if len(self.num) % 2 == 0:
            for n in range(len(self.num)/2):
                if self.num[n] == self.num[-n-1]:
                    pass
                else:
                    return False
        else:
            for n in range((len(self.num)-1)/2):
                if self.num[n] == self.num[-n - 1]:
                    pass
                else:
                    return False
        return True

if __name__ == '__main__':
    num = '12355321'
    s = Solution(num)
    print s.palindrome_number()
