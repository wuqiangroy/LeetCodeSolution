#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5
(not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):

    def __init__(self, lst):
        self.lst = list(lst)

    def buy_and_sell(self):
        n = 0
        res = []
        while n < len(self.lst)-1:
            for j in xrange(n, len(self.lst)):
                res.append(self.lst[j] - self.lst[n])
            n += 1
        return max(res)

if __name__ == '__main__':
    lst = [5, 6, 7, 9, 5, 13, 11, 10, 22, 17]
    s = Solution(lst)
    print s.buy_and_sell()