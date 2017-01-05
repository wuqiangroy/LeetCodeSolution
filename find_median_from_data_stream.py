#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3)
findMedian() -> 2

"""


class MedianFinder(object):
    def __init__(self):
        self.num = []

    def add_num(self, num):
        self.num.append(int(num))

    def find_median(self):
        if len(self.num) % 2 != 0:
            return self.num[(len(self.num)-1)/2]
        else:
            return float(self.num[(len(self.num)/2)-1] + self.num[(len(self.num)/2)]) / 2

m = MedianFinder()
m.add_num(1)
m.add_num(2)
m.add_num(3)
m.add_num(4)
print m.find_median()


