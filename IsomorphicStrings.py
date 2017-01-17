#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character
while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""


class Solution(object):

    def __init__(self, s1, s2):
        self.s1 = str(s1)
        self.s2 = str(s2)

    def isomorphic_strings(self):
        if len(self.s1) != len(self.s2):
            return False
        i = 0
        while i < len(self.s1)-1:
            for j in xrange(i+1, len(self.s1)):
                if self.s1[i] == self.s1[j] and self.s2[i] == self.s2[j]:
                    return True
                elif self.s1[i] != self.s1[j] and self.s2[i] != self.s2[j]:
                    continue
                elif self.s1[i] == self.s1[j] and self.s2[i] != self.s2[j] or \
                        self.s1[i] != self.s1[j] and self.s2[i] == self.s2[j]:
                    return False
            i += 1

if __name__ == '__main__':
    s1 = 'foo'
    s2 = 'lee'
    s = Solution(s1, s2)
    print s.isomorphic_strings()
