# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:14:25 2019

@author: user
"""

class Solution:
    def ReverseList(self,pHead):
        if not pHead or not pHead.next:
            return pHead
        #新的表头
        newhead = None
        #临时变量
        tmp = None
        while pHead:
            tmp = pHead.next
            pHead.next = newhead
            newhead = pHead
            pHead = tmp
        return newhead