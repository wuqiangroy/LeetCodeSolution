#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
Given a string array words, find the maximum value of
length(word[i])*length(word[j]) where the two words do not share common letters.
You may assume that each word will contain only lower case letters.
If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""


def common_letters(n1, n2):
    for i in n1:
        if i in n2:
            return False
    return True


def maximum_lengths(lst):
    try:
        if len(lst) < 2:
            return 0
        res = []
        for i in range(len(lst)-1):
            for j in range(i+1, len(lst)):
                if common_letters(lst[i], lst[j]):
                    res.append(len(lst[i])*len(lst[j]))
        if res:
            return max(res)
        return 0
    except TypeError:
        return 'please enter string'

if __name__ == '__main__':
    lst = ['wuqiang', 'zhangwenwen', 'zz']
    print maximum_lengths(lst)
