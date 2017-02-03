#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given an array of integers,
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
# 1


class Solution(object):

    def __init__(self, lst, target):
        self.lst = list(lst)
        self.lst.sort()
        self.target = int(target)

    def TwoSum(self):
        for n1 in range(len(self.lst)-1):
            for n2 in range(n1+1, len(self.lst)):
                if self.lst[n1] + self.lst[n2] == self.target:
                    return [n1+1, n2+1]

# 2


def twoSum(numbers, target):
    # write your code here
    n = 0
    while n < len(numbers):
        new_lst = [x for x in numbers]
        new_lst.pop(n)
        num = target - numbers[n]
        if num in new_lst:
            return [n + 1, new_lst.index(num) + 2]
        n += 1

if __name__ == '__main__':
    from timeit import Timer
    lst = [1, 3, 5, 6, 7, 8, 9]
    target = 11
    lst2 = [1, 0, -1]
    target2 = -1
    s = Solution(lst, target)
    print s.TwoSum()
    print twoSum(lst2, target2)

    t1 = Timer(lambda: s.TwoSum())
    t2 = Timer(lambda: twoSum(lst2, target2))
    print t1.timeit(1000000)
    print t2.timeit(1000000)
