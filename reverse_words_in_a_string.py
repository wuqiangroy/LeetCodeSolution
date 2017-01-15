#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""


class Solution(object):

    def reverse_words(self, words):
        new_words = words.split(' ')
        if len(new_words) % 2 == 0:
            for n in xrange(len(new_words)/2):
                new_words[n], new_words[-1-n] = new_words[-1-n], new_words[n]
        else:
            for n in xrange((len(new_words)-1)/2):
                new_words[n], new_words[-1 - n] = new_words[-1 - n], new_words[n]
        return new_words

    def reverse_words2(self, words):
        new_words = words.split(' ')
        new_words.reverse()
        return new_words

if __name__ == '__main__':
    words = 'fighting is a bright atitute'
    s = Solution()
    print s.reverse_words(words)
    print s.reverse_words2(words)