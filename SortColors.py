#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent
the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""

# 冒泡排序


class BubbleSort(object):

    def __init__(self, lst):
        self.lst = list(lst)

    def sort_colors(self):
        for i in range(len(self.lst)-1, 0, -1):
            for n in xrange(i):
                if self.lst[n+1] < self.lst[n]:
                    self.lst[n], self.lst[n+1] = self.lst[n+1], self.lst[n]
        return self.lst

    def sort_colors2(self):
        n = 0
        while n < len(self.lst):
            for j in xrange(len(self.lst)-1):
                if self.lst[j+1] < self.lst[j]:
                    self.lst[j], self.lst[j+1] = self.lst[j+1], self.lst[j]
            n += 1
        return self.lst


# 选择排序


class SelectSort(object):

    def __init__(self, lst):
        self.lst = list(lst)

    def sort_colors(self):
        res = []
        for n in range(len(self.lst)):
            res.append(min(self.lst))       # 在新建res列表中加入已知列表的最小数
            self.lst.pop(self.lst.index(min(self.lst)))         # 删掉已知列表最小数
        return res

# 插入排序


class InsertSort(object):

    def __init__(self, lst):
        self.lst = list(lst)

    def sort_colors(self):
        if len(self.lst) == 1:
            return lst

        for i in range(1, len(self.lst)):
            for j in range(i, 0, -1):
                if self.lst[j] < self.lst[j - 1]:
                    self.lst[j], self.lst[j - 1] = self.lst[j - 1], self.lst[j]
        return self.lst

if __name__ == '__main__':
    lst = [1, 0, 2, 0, 1, 2, 1, 1, 0, 0, 2]
    s = BubbleSort(lst)
    print s.sort_colors2()
    sel = SelectSort(lst)
    print sel.sort_colors()
    ins = InsertSort(lst)
    print ins.sort_colors()