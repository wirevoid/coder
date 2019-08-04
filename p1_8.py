# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:41:11 2019

@author: user
"""

class Solution:
    def Mirror(self,root):
        tmp = None
        if root != None:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.Mirror(root.left)
            self.Mirror(root.right)
            