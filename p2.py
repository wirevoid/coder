# -*- coding: utf-8 -*-
"""
Created on Sun May 19 10:59:55 2019

@author: user
"""

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s.replace(' ','%20')
        return s
while True:
    try:
        S = Solution()
        s = input()
        print(S.replaceSpace(s))
    except:
        break