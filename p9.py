# -*- coding: utf-8 -*-
"""
Created on Sat May 25 21:30:12 2019

@author: user
"""

class Solution:
    def Transform(self,n):
        count = 0
        if n<0:
            n = n&0xffffffff
        while n:
            count =+ 1
            n = (n-1)&n
        return count