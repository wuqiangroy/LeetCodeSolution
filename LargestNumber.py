#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

"""
"""
这一段是别人的代码，自己考虑了很久也放了上来，主要是cmp（x+y，y+x）思考了很久。

"""


class Solution(object):
    def largest_number(self, num):
        lis_num = [str(x) for x in num]     # 将遍历的num中数变为str
        lis_num.sort(lambda x, y: cmp(y+x, x+y))    # 自定义函数，当前str加上后str大于后str加上前str是，排列。
        # 比如：'30'和'3'排列，'30'+'3'='303'， '3'+'30'='330',cmp（'303','330')=-1， 所以'3'排在'30'前面
        return ''.join(lis_num)


s = Solution()
print s.largest_number([30, 8, 3, 2])
