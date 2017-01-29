#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins
that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins,
return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""

res = []


def coin_change(coins, amount, value=0, n=1):
    global res
    for i in coins:
        if value + i == amount:
            res.append(n)
            return n
        coin_change(coins, amount, value=value+i, n=n+1)
    if res is None:
        return -1
    return min(res)

if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print coin_change(coins, amount)
