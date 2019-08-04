# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:23:33 2019

@author: user
"""
#解题思路：用python的话暴力搜索
"""
思路1 每一行都是递增数组，遍历所有行用二分查找
思路2 在数组中，左下角的元素一定比x小   选取右上角 
"""

class Solution():
    def Find(self,target,array):
        n = len(array)
        flag = 'false'
        for i in range(n):
            if target in array[i]:
                flag = 'true'
                break
        return flag

while True:
    try:
        L = list(eval(raw_input()))
        S = Solution()
        target = L[0]
        array = L[1]
        print(S.Find(target,array))
    except:
        break