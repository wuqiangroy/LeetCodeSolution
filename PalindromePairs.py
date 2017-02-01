#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given a list of unique words, find all pairs of distinct indices
(i, j) in the given list, so that the concatenation of the two words,
 i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""


def determine_palindrome(i):
    i2 = reversed(i)
    res = []
    for j in i2:
        res.append(j)
    if i == ''.join(res):
        return True


def palindrome_pairs(lst):
    try:
        res = []
        n = 0
        while n < len(lst)-1:
            for j in range(n+1, len(lst)):
                if determine_palindrome(lst[n]+lst[j]):
                    res.append([n, j])
                if determine_palindrome(lst[j]+lst[n]):
                    res.append([j, n])
            n += 1
        if res:
            return res
        return False
    except TypeError:
        return 'wrong type'

if __name__ == '__main__':
    lst = ["bat", "tab", "cat"]
    lst2 = [1, 2, 3, 4]
    print palindrome_pairs(lst2)
