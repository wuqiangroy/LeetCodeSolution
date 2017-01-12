#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Given two words word1 and word2,
find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""


class Solution(object):

    def __init__(self, word1, word2):
        self.word1 = list(word1)
        self.word2 = list(word2)

    def edit_distance(self):
        if len(self.word1) >= len(self.word2):
            for n in range(len(self.word2)):
                if self.word1[n] != self.word2[n]:
                    self.word1[n] = self.word2[n]
            del self.word1[len(self.word2):]
            return ''.join(self.word1)

        else:
            for n in range(len(self.word2)):
                try:
                    if self.word1[n] != self.word2[n]:
                        self.word1[n] = self.word2[n]
                except IndexError:
                    self.word1.insert(n, self.word2[n])
            return ''.join(self.word1)

if __name__ =='__main__':
    word1 = 'wuqiangroy'
    word2 = 'zhangwenwen'
    s = Solution(word1, word2)
    print s.edit_distance()

