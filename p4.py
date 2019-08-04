# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:37:10 2019

@author: user
"""

#采用递归的方法，首先在前序遍历中得到当前子树的根节点，通过根节点在中序序列中的位置划分出左右子树包含的节点

class Solution:
    def reConstructBinaryTree(self,pre,tin):
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        pos = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:1+pos],tin[:pos])
        root.right = self.reConstructBinaryTree(pre[pos+1:],tin[pos+1:])
        return root